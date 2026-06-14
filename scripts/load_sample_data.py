"""Test utilities and sample data loader"""
from models import SessionLocal, init_db
from models.ingredient import Ingredient, Certification, Allergen
from models.dish import Dish, DishIngredient
from datetime import datetime, timedelta
from config import AVAILABLE_CERTIFICATIONS, COMMON_ALLERGENS

def load_sample_data():
    """Load sample data into the database"""
    db = SessionLocal()
    init_db()
    
    # Clear existing data
    db.query(DishIngredient).delete()
    db.query(Dish).delete()
    db.query(Ingredient).delete()
    db.query(Certification).delete()
    db.query(Allergen).delete()
    db.commit()
    
    # Create certifications
    certs = {}
    for cert_name in ["Organic", "Local", "Fair Trade", "Wild-Caught", "Free-Range", "Grass-Fed"]:
        cert = Certification(name=cert_name)
        db.add(cert)
        db.flush()
        certs[cert_name] = cert
    
    # Create allergens
    allergens = {}
    for allergen_name in ["Milk", "Eggs", "Fish", "Shellfish"]:
        allergen = Allergen(name=allergen_name)
        db.add(allergen)
        db.flush()
        allergens[allergen_name] = allergen
    
    # Create ingredients
    romaine = Ingredient(
        name="Romaine Lettuce",
        quality_score=95,
        max_days=5,
        days_fresh=2,
        harvest_date=datetime.now() - timedelta(days=1),
        source_location="Local Farm - Sunrise Valley",
        quantity_unit="grams",
        is_organic=True,
        is_local=True,
        price_per_unit=0.05
    )
    romaine.certifications.append(certs["Organic"])
    romaine.certifications.append(certs["Local"])
    db.add(romaine)
    
    parmesan = Ingredient(
        name="Parmesan Cheese",
        quality_score=92,
        max_days=30,
        days_fresh=12,
        harvest_date=datetime.now() - timedelta(days=18),
        source_location="Artisan Dairy Co.",
        quantity_unit="grams",
        price_per_unit=0.50
    )
    parmesan.allergens.append(allergens["Milk"])
    db.add(parmesan)
    
    salmon = Ingredient(
        name="Atlantic Salmon",
        quality_score=98,
        max_days=3,
        days_fresh=1,
        harvest_date=datetime.now() - timedelta(days=1),
        source_location="Norwegian Fjord Farms",
        quantity_unit="grams",
        price_per_unit=1.50
    )
    salmon.certifications.append(certs["Wild-Caught"])
    salmon.allergens.append(allergens["Fish"])
    db.add(salmon)
    
    db.commit()
    
    # Create dishes
    caesar_salad = Dish(
        name="Caesar Salad",
        description="Fresh romaine lettuce with aged parmesan and homemade croutons",
        price=12.99,
        category="salad",
        is_available=1,
        preparation_time=5,
        calories=250
    )
    db.add(caesar_salad)
    db.flush()
    
    DishIngredient(dish_id=caesar_salad.id, ingredient_id=romaine.id, quantity=200, unit="grams")
    DishIngredient(dish_id=caesar_salad.id, ingredient_id=parmesan.id, quantity=40, unit="grams")
    
    grilled_salmon = Dish(
        name="Grilled Salmon",
        description="Fresh Atlantic salmon with seasonal vegetables",
        price=24.99,
        category="main",
        is_available=1,
        preparation_time=15,
        calories=450
    )
    db.add(grilled_salmon)
    db.flush()
    
    DishIngredient(dish_id=grilled_salmon.id, ingredient_id=salmon.id, quantity=180, unit="grams")
    
    db.commit()
    print("Sample data loaded successfully!")
    db.close()

if __name__ == "__main__":
    load_sample_data()

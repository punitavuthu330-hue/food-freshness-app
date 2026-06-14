"""FastAPI backend for Fresh & Fair app"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models import SessionLocal, init_db
from models.ingredient import Ingredient, Certification, Allergen
from models.dish import Dish, DishIngredient, DishReview
from models.user import User, UserPreference
from models.order import Order, OrderItem
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fresh & Fair API",
    description="Food Freshness & Quality Transparency API",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    """Initialize database on startup"""
    init_db()
    logger.info("Database initialized")

# Health check
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# ==================== INGREDIENT ENDPOINTS ====================

@app.get("/api/ingredients")
def list_ingredients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List all ingredients"""
    ingredients = db.query(Ingredient).offset(skip).limit(limit).all()
    return {
        "total": db.query(Ingredient).count(),
        "items": ingredients
    }

@app.get("/api/ingredients/{ingredient_id}")
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    """Get single ingredient"""
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@app.post("/api/ingredients")
def create_ingredient(name: str, quality_score: float, max_days: int, db: Session = Depends(get_db)):
    """Create new ingredient"""
    ingredient = Ingredient(
        name=name,
        quality_score=quality_score,
        max_days=max_days,
        days_fresh=max_days,
        harvest_date=datetime.utcnow(),
        quantity_unit="grams"
    )
    db.add(ingredient)
    db.commit()
    db.refresh(ingredient)
    return ingredient

# ==================== DISH ENDPOINTS ====================

@app.get("/api/dishes")
def list_dishes(category: str = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List all dishes with optional category filter"""
    query = db.query(Dish).filter(Dish.is_available == 1)
    if category:
        query = query.filter(Dish.category == category)
    
    dishes = query.offset(skip).limit(limit).all()
    return {
        "total": query.count(),
        "items": dishes
    }

@app.get("/api/dishes/{dish_id}")
def get_dish(dish_id: int, db: Session = Depends(get_db)):
    """Get single dish with ingredients"""
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    
    ingredients_data = []
    for di in dish.ingredients:
        ingredients_data.append({
            "id": di.ingredient.id,
            "name": di.ingredient.name,
            "quantity": di.quantity,
            "unit": di.unit,
            "quality_score": di.ingredient.quality_score,
            "days_fresh": di.ingredient.days_fresh,
            "max_days": di.ingredient.max_days,
            "source_location": di.ingredient.source_location
        })
    
    return {
        "id": dish.id,
        "name": dish.name,
        "description": dish.description,
        "price": dish.price,
        "category": dish.category,
        "preparation_time": dish.preparation_time,
        "calories": dish.calories,
        "ingredients": ingredients_data
    }

@app.get("/api/dishes/{dish_id}/freshness")
def get_dish_freshness(dish_id: int, db: Session = Depends(get_db)):
    """Get freshness metrics for a dish"""
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    
    from utils.freshness import get_freshness_status, calculate_average_freshness, calculate_average_quality
    
    ingredients_list = []
    for di in dish.ingredients:
        ing = di.ingredient
        status = get_freshness_status(ing.days_fresh, ing.max_days)
        ingredients_list.append({
            "name": ing.name,
            "freshness_status": status,
            "quality_score": ing.quality_score,
            "days_fresh": ing.days_fresh,
            "max_days": ing.max_days
        })
    
    avg_quality = calculate_average_quality([{"quality_score": ing.ingredient.quality_score} for ing in dish.ingredients])
    premium_count = sum(1 for di in dish.ingredients if di.ingredient.quality_score >= 90)
    
    return {
        "dish_id": dish.id,
        "dish_name": dish.name,
        "ingredients": ingredients_list,
        "average_quality": avg_quality,
        "premium_ingredients": premium_count,
        "total_ingredients": len(dish.ingredients)
    }

# ==================== MENU ENDPOINT ====================

@app.get("/api/menu")
def get_menu(min_quality: int = 0, db: Session = Depends(get_db)):
    """Get full menu with quality filtering"""
    from utils.freshness import get_freshness_status
    
    dishes = db.query(Dish).filter(Dish.is_available == 1).all()
    menu_items = []
    
    for dish in dishes:
        # Filter by quality threshold
        ingredients = dish.ingredients
        avg_quality = sum(ing.ingredient.quality_score for ing in ingredients) / len(ingredients) if ingredients else 0
        
        if avg_quality < min_quality:
            continue
        
        # Build ingredient details
        ingredient_details = []
        for di in ingredients:
            ing = di.ingredient
            freshness_status = get_freshness_status(ing.days_fresh, ing.max_days)
            ingredient_details.append({
                "name": ing.name,
                "quantity": f"{di.quantity} {di.unit}",
                "sourced": ing.source_location,
                "quality_score": ing.quality_score,
                "days_fresh": ing.days_fresh,
                "max_days": ing.max_days,
                "freshness_status": freshness_status,
                "certifications": [c.name for c in ing.certifications]
            })
        
        menu_items.append({
            "id": dish.id,
            "name": dish.name,
            "price": dish.price,
            "description": dish.description,
            "category": dish.category,
            "average_quality": round(avg_quality, 2),
            "premium_ingredients": sum(1 for ing in ingredients if ing.ingredient.quality_score >= 90),
            "ingredients": ingredient_details
        })
    
    return {
        "total_items": len(menu_items),
        "menu": menu_items
    }

# ==================== CERTIFICATION ENDPOINTS ====================

@app.get("/api/certifications")
def list_certifications(db: Session = Depends(get_db)):
    """List all certifications"""
    certifications = db.query(Certification).all()
    return {"items": certifications}

# ==================== ALLERGEN ENDPOINTS ====================

@app.get("/api/allergens")
def list_allergens(db: Session = Depends(get_db)):
    """List all allergens"""
    allergens = db.query(Allergen).all()
    return {"items": allergens}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

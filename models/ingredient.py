"""Ingredient model"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from models import Base

# Association table for many-to-many relationship between Ingredients and Certifications
ingredient_certification = Table(
    'ingredient_certification',
    Base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('certification_id', Integer, ForeignKey('certification.id'))
)

ingredient_allergen = Table(
    'ingredient_allergen',
    Base.metadata,
    Column('ingredient_id', Integer, ForeignKey('ingredient.id')),
    Column('allergen_id', Integer, ForeignKey('allergen.id'))
)

class Ingredient(Base):
    __tablename__ = "ingredient"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(String(500), nullable=True)
    quantity_unit = Column(String(50))  # grams, ml, pieces, etc.
    source_location = Column(String(255))  # farm or supplier location
    quality_score = Column(Float, default=80.0)  # 0-100
    harvest_date = Column(DateTime, default=datetime.utcnow)
    days_fresh = Column(Integer)  # days remaining
    max_days = Column(Integer)  # maximum shelf life days
    is_organic = Column(Boolean, default=False)
    is_local = Column(Boolean, default=False)
    price_per_unit = Column(Float, nullable=True)
    supplier_name = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    certifications = relationship(
        "Certification",
        secondary=ingredient_certification,
        back_populates="ingredients"
    )
    allergens = relationship(
        "Allergen",
        secondary=ingredient_allergen,
        back_populates="ingredients"
    )
    dish_ingredients = relationship("DishIngredient", back_populates="ingredient")
    quality_history = relationship("QualityHistory", back_populates="ingredient", cascade="all, delete-orphan")

class Certification(Base):
    __tablename__ = "certification"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(String(500), nullable=True)
    
    ingredients = relationship(
        "Ingredient",
        secondary=ingredient_certification,
        back_populates="certifications"
    )

class Allergen(Base):
    __tablename__ = "allergen"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(String(500), nullable=True)
    
    ingredients = relationship(
        "Ingredient",
        secondary=ingredient_allergen,
        back_populates="allergens"
    )

class QualityHistory(Base):
    __tablename__ = "quality_history"
    
    id = Column(Integer, primary_key=True, index=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), index=True)
    quality_score = Column(Float)
    days_fresh = Column(Integer)
    recorded_at = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(500), nullable=True)
    
    ingredient = relationship("Ingredient", back_populates="quality_history")

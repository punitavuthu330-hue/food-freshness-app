"""Dish model"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from models import Base

class Dish(Base):
    __tablename__ = "dish"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    description = Column(String(1000), nullable=True)
    price = Column(Float)
    category = Column(String(100))  # appetizer, main, dessert, etc.
    is_available = Column(Integer, default=1)  # boolean
    preparation_time = Column(Integer, nullable=True)  # minutes
    calories = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    ingredients = relationship("DishIngredient", back_populates="dish", cascade="all, delete-orphan")
    reviews = relationship("DishReview", back_populates="dish", cascade="all, delete-orphan")

class DishIngredient(Base):
    __tablename__ = "dish_ingredient"
    
    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey('dish.id'), index=True)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'), index=True)
    quantity = Column(Float)
    unit = Column(String(50))  # grams, ml, pieces, etc.
    
    # Relationships
    dish = relationship("Dish", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="dish_ingredients")

class DishReview(Base):
    __tablename__ = "dish_review"
    
    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey('dish.id'), index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    rating = Column(Integer)  # 1-5
    freshness_rating = Column(Integer, nullable=True)  # 1-5
    quality_comment = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    dish = relationship("Dish", back_populates="reviews")
    user = relationship("User", back_populates="reviews")

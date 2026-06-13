"""User model for authentication and preferences"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan", uselist=False)
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("DishReview", back_populates="user", cascade="all, delete-orphan")

class UserPreference(Base):
    __tablename__ = "user_preference"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True, index=True)
    min_quality_score = Column(Integer, default=80)
    preferred_certifications = Column(Text, nullable=True)  # JSON string
    avoided_allergens = Column(Text, nullable=True)  # JSON string
    dietary_restrictions = Column(Text, nullable=True)  # JSON string
    theme = Column(String(50), default="light")
    notifications_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="preferences")

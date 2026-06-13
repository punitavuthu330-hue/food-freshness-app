"""Order model"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from models import Base

class OrderStatus(PyEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Order(Base):
    __tablename__ = "order"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    order_number = Column(String(50), unique=True, index=True)
    status = Column(String(20), default=OrderStatus.PENDING.value)
    total_price = Column(Float)
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_item"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('order.id'), index=True)
    dish_id = Column(Integer, ForeignKey('dish.id'), nullable=True)
    dish_name = Column(String(255))  # Snapshot of dish name
    quantity = Column(Integer)
    price_per_unit = Column(Float)
    special_requests = Column(String(500), nullable=True)
    
    # Relationships
    order = relationship("Order", back_populates="items")

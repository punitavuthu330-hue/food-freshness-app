"""Input validation utilities"""
from datetime import datetime
import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_username(username):
    """Validate username format"""
    if len(username) < 3 or len(username) > 50:
        return False
    pattern = r'^[a-zA-Z0-9_-]+$'
    return re.match(pattern, username) is not None

def validate_quality_score(score):
    """Validate quality score (0-100)"""
    try:
        score = float(score)
        return 0 <= score <= 100
    except (ValueError, TypeError):
        return False

def validate_days_fresh(days_fresh, max_days):
    """Validate days fresh is less than max days"""
    try:
        days_fresh = int(days_fresh)
        max_days = int(max_days)
        return 0 <= days_fresh <= max_days and max_days > 0
    except (ValueError, TypeError):
        return False

def validate_price(price):
    """Validate price is positive"""
    try:
        price = float(price)
        return price > 0
    except (ValueError, TypeError):
        return False

def validate_rating(rating):
    """Validate rating (1-5)"""
    try:
        rating = int(rating)
        return 1 <= rating <= 5
    except (ValueError, TypeError):
        return False

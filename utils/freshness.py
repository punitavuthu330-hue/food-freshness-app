"""Freshness calculation utilities"""
from config import FRESHNESS_THRESHOLDS, FRESHNESS_COLORS

def calculate_freshness_ratio(days_fresh, max_days):
    """Calculate freshness ratio (0-1)"""
    if max_days == 0:
        return 0
    return days_fresh / max_days

def get_freshness_status(days_fresh, max_days):
    """Determine freshness status based on days remaining"""
    ratio = calculate_freshness_ratio(days_fresh, max_days)
    
    if ratio >= FRESHNESS_THRESHOLDS["excellent"]:
        return "excellent"
    elif ratio >= FRESHNESS_THRESHOLDS["good"]:
        return "good"
    elif ratio >= FRESHNESS_THRESHOLDS["fair"]:
        return "fair"
    else:
        return "poor"

def get_freshness_display(status):
    """Get display info for freshness status"""
    return FRESHNESS_COLORS.get(status, FRESHNESS_COLORS["poor"])

def calculate_average_freshness(ingredients_list):
    """Calculate average freshness across multiple ingredients"""
    if not ingredients_list:
        return 0
    total_ratio = sum(
        calculate_freshness_ratio(ing.get('days_fresh', 0), ing.get('max_days', 1))
        for ing in ingredients_list
    )
    return (total_ratio / len(ingredients_list)) * 100

def calculate_average_quality(ingredients_list):
    """Calculate average quality score across multiple ingredients"""
    if not ingredients_list:
        return 0
    total_quality = sum(ing.get('quality_score', 0) for ing in ingredients_list)
    return total_quality / len(ingredients_list)

def count_premium_ingredients(ingredients_list, threshold=90):
    """Count ingredients above quality threshold"""
    return sum(1 for ing in ingredients_list if ing.get('quality_score', 0) >= threshold)

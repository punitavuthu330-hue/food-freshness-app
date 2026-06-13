"""Configuration settings for Fresh & Fair app"""
import os
from pathlib import Path

# App settings
APP_NAME = "Fresh & Fair"
APP_DESCRIPTION = "Food Freshness & Quality Transparency App"
APP_VERSION = "1.0.0"

# Paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
DB_DIR = DATA_DIR / "database"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)
DB_DIR.mkdir(exist_ok=True)

# Database settings
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_DIR}/freshness_app.db")

# Freshness thresholds
FRESHNESS_THRESHOLDS = {
    "excellent": 0.7,  # >= 70% of shelf life
    "good": 0.4,       # >= 40% of shelf life
    "fair": 0.2,       # >= 20% of shelf life
    "poor": 0.0        # < 20% of shelf life
}

FRESHNESS_COLORS = {
    "excellent": {"bg": "#d4edda", "border": "#28a745", "emoji": "🟢"},
    "good": {"bg": "#cfe2ff", "border": "#0d6efd", "emoji": "🟡"},
    "fair": {"bg": "#fff3cd", "border": "#ffc107", "emoji": "🟠"},
    "poor": {"bg": "#f8d7da", "border": "#dc3545", "emoji": "🔴"}
}

# Quality score thresholds
QUALITY_THRESHOLDS = {
    "premium": 90,
    "high": 75,
    "medium": 50,
    "low": 0
}

# Certifications
AVAILABLE_CERTIFICATIONS = [
    "Organic",
    "Fair Trade",
    "Local",
    "GMO-Free",
    "Gluten-Free",
    "Vegan",
    "Wild-Caught",
    "Free-Range",
    "Grass-Fed",
    "Cold Pressed"
]

# Allergens
COMMON_ALLERGENS = [
    "Peanuts",
    "Tree Nuts",
    "Milk",
    "Eggs",
    "Fish",
    "Shellfish",
    "Soy",
    "Wheat",
    "Sesame"
]

# API settings (for future backend integration)
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_KEY = os.getenv("API_KEY", "")

# UI settings
UI_THEME = "light"
PAGE_ICON = "🥗"
WIDE_LAYOUT = True

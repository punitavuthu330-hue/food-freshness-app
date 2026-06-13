# Fresh & Fair - Food Freshness & Quality Transparency App

## Overview

**Fresh & Fair** is an interactive prototype app that solves customer visibility issues around food freshness and quality at the point of ordering. Customers can now verify ingredient sourcing, assess quality before purchase, and understand exactly what they're getting.

## Problem Solved

- ❌ **Before:** Customers couldn't verify when ingredients were sourced or assess quality before buying
- ✅ **After:** Complete transparency on every ingredient—harvest dates, quality scores, sourcing, and certifications

## Key Features

### 1. **Quality Score Filtering**
- Sidebar filter to show only dishes that meet minimum quality thresholds
- Ensures customers only see ingredients within their standards

### 2. **Ingredient Transparency**
For each ingredient, customers can see:
- **Source Location:** Exact farm or supplier
- **Harvest Date:** When it was sourced
- **Freshness Status:** Days remaining vs. maximum shelf life (Excellent 🟢 / Good 🟡 / Fair 🟠 / Poor 🔴)
- **Quality Score:** 0-100 rating
- **Certifications:** Organic, Fair Trade, Local, etc.

### 3. **Visual Dashboards**
- **Ingredient Freshness Chart:** Bar chart showing freshness % and quality for all ingredients in a dish
- **Quality Gauges:** Color-coded indicators for quality metrics
- **Overall Dish Metrics:** Average quality score and premium ingredient count

### 4. **Interactive Menu Browsing**
- Expandable menu items with detailed breakdowns
- Color-coded freshness indicators (green = excellent, yellow = good, orange = fair, red = poor)
- Detailed ingredient analysis with certifications

### 5. **Freshness Status Indicators**
- **Excellent (🟢):** 70%+ of shelf life remaining
- **Good (🟡):** 40-70% remaining
- **Fair (🟠):** 20-40% remaining
- **Poor (🔴):** <20% remaining

## Sample Data Included

The app comes with 4 demo dishes:
1. **Caesar Salad** - Local, organic ingredients with excellent freshness
2. **Grilled Salmon** - Wild-caught, premium sourcing with top quality
3. **Vegetable Stir Fry** - Seasonal vegetables from local farms
4. **Chocolate Torte** - Fair trade chocolate and artisan ingredients

Each includes realistic harvest dates, sourcing information, and quality metrics.

## Installation & Running

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run food_freshness_app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. **View Menu:** Browse available dishes in the main area
2. **Filter by Quality:** Use the sidebar to set minimum quality score (0-100)
3. **Expand Dish Details:** Click any dish to see ingredient breakdown
4. **Analyze Ingredients:** View freshness charts, quality scores, and sourcing for each ingredient
5. **Review Certifications:** See organic, fair trade, local, and other certifications
6. **Make Informed Decision:** Use the complete transparency to decide what to order

## Architecture & Design

### Data Model
- Menu items with prices
- Ingredients with metadata:
  - Quantity and unit
  - Source/supplier
  - Days fresh (remaining) and max days
  - Quality score (0-100)
  - Harvest date
  - Certifications/labels

### Frontend Components
- **Sidebar:** Filter controls and configuration
- **Expanders:** Collapsible menu items
- **Charts:** Plotly-based visualizations
- **Data Tables:** Clean ingredient breakdowns
- **Color-coded Cards:** Visual freshness indicators
- **Call-to-Action Buttons:** Order, ask about origin, nutrition info

## Extensibility

### Easy to Extend With:
- **Real Database:** Connect to restaurant POS/inventory system
- **Live Freshness Updates:** Integrate with IoT sensors or inventory management
- **User Accounts:** Save preferences and order history
- **Allergen Information:** Add allergen warnings
- **Nutritional Data:** Display detailed nutrition facts
- **Reviews:** Customer ratings and comments on freshness
- **Real-time Availability:** Show which dishes are available now
- **Pricing Tiers:** Different prices based on ingredient freshness levels
- **Farm Integration:** Direct links to farm/supplier information
- **Supply Chain Tracking:** QR codes or blockchain verification

## Technology Stack

- **Streamlit:** Interactive web UI framework
- **Pandas:** Data manipulation and analysis
- **Plotly:** Interactive charts and visualizations
- **Python 3.8+:** Core language

## Future Enhancements

- [ ] Integration with restaurant management systems
- [ ] Real-time inventory and freshness data
- [ ] QR code scanning for instant ingredient info
- [ ] User accounts and preference saving
- [ ] API for third-party integrations
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Allergen and dietary restriction filtering
- [ ] AI-powered recommendations based on freshness preferences
- [ ] Carbon footprint tracking for sourcing impact

## Contact & Feedback

For questions or suggestions about this prototype, contact:
**Email:** pavanreddy.avuthu@gmail.com

---

**Fresh & Fair** - *Transparency from farm to table* 🌱
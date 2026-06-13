import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Fresh & Fair - Food Quality Transparency",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .freshness-excellent { background-color: #d4edda; padding: 10px; border-radius: 5px; border-left: 5px solid #28a745; }
    .freshness-good { background-color: #cfe2ff; padding: 10px; border-radius: 5px; border-left: 5px solid #0d6efd; }
    .freshness-fair { background-color: #fff3cd; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; }
    .freshness-poor { background-color: #f8d7da; padding: 10px; border-radius: 5px; border-left: 5px solid #dc3545; }
    .metric-box { background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Sample data - restaurant menu with ingredient freshness
MENU_DATA = {
    "Caesar Salad": {
        "price": "$12.99",
        "ingredients": {
            "Romaine Lettuce": {
                "quantity": "200g",
                "sourced": "Local Farm - Sunrise Valley",
                "days_fresh": 2,
                "max_days": 5,
                "quality_score": 95,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Organic", "Local"]
            },
            "Parmesan Cheese": {
                "quantity": "40g",
                "sourced": "Artisan Dairy Co.",
                "days_fresh": 12,
                "max_days": 30,
                "quality_score": 92,
                "harvest_date": (datetime.now() - timedelta(days=18)).strftime("%Y-%m-%d"),
                "certifications": ["Aged 24 months"]
            },
            "Croutons": {
                "quantity": "30g",
                "sourced": "In-house production",
                "days_fresh": 5,
                "max_days": 7,
                "quality_score": 88,
                "harvest_date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
                "certifications": ["Made Daily"]
            },
            "Caesar Dressing": {
                "quantity": "60ml",
                "sourced": "Premium Pantry",
                "days_fresh": 20,
                "max_days": 45,
                "quality_score": 85,
                "harvest_date": (datetime.now() - timedelta(days=25)).strftime("%Y-%m-%d"),
                "certifications": ["No MSG"]
            }
        }
    },
    "Grilled Salmon": {
        "price": "$24.99",
        "ingredients": {
            "Atlantic Salmon": {
                "quantity": "180g",
                "sourced": "Norwegian Fjord Farms",
                "days_fresh": 1,
                "max_days": 3,
                "quality_score": 98,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Wild-Caught", "MSC Certified"]
            },
            "Lemon": {
                "quantity": "1/4",
                "sourced": "California Citrus Grove",
                "days_fresh": 6,
                "max_days": 14,
                "quality_score": 91,
                "harvest_date": (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d"),
                "certifications": ["Organic"]
            },
            "Asparagus": {
                "quantity": "150g",
                "sourced": "Local Farm - Sunrise Valley",
                "days_fresh": 2,
                "max_days": 5,
                "quality_score": 94,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Organic", "Local"]
            },
            "Olive Oil": {
                "quantity": "15ml",
                "sourced": "Italian Estate",
                "days_fresh": 180,
                "max_days": 730,
                "quality_score": 96,
                "harvest_date": (datetime.now() - timedelta(days=120)).strftime("%Y-%m-%d"),
                "certifications": ["Extra Virgin", "Cold Pressed"]
            }
        }
    },
    "Vegetable Stir Fry": {
        "price": "$14.99",
        "ingredients": {
            "Broccoli": {
                "quantity": "120g",
                "sourced": "Local Farm - Green Valley",
                "days_fresh": 2,
                "max_days": 7,
                "quality_score": 93,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Organic"]
            },
            "Bell Peppers": {
                "quantity": "150g",
                "sourced": "Local Farm - Green Valley",
                "days_fresh": 3,
                "max_days": 10,
                "quality_score": 89,
                "harvest_date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
                "certifications": ["Local"]
            },
            "Snap Peas": {
                "quantity": "100g",
                "sourced": "Local Farm - Sunrise Valley",
                "days_fresh": 2,
                "max_days": 5,
                "quality_score": 90,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Organic", "Local"]
            },
            "Garlic": {
                "quantity": "3 cloves",
                "sourced": "California Garlic Farm",
                "days_fresh": 45,
                "max_days": 180,
                "quality_score": 87,
                "harvest_date": (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d"),
                "certifications": ["Organic"]
            }
        }
    },
    "Chocolate Torte": {
        "price": "$9.99",
        "ingredients": {
            "Dark Chocolate": {
                "quantity": "100g",
                "sourced": "Fair Trade Chocolatier",
                "days_fresh": 90,
                "max_days": 365,
                "quality_score": 94,
                "harvest_date": (datetime.now() - timedelta(days=45)).strftime("%Y-%m-%d"),
                "certifications": ["Fair Trade", "70% Cacao"]
            },
            "Eggs": {
                "quantity": "2",
                "sourced": "Free-Range Farm",
                "days_fresh": 3,
                "max_days": 14,
                "quality_score": 92,
                "harvest_date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
                "certifications": ["Free-Range", "Organic"]
            },
            "Butter": {
                "quantity": "50g",
                "sourced": "Artisan Dairy Co.",
                "days_fresh": 20,
                "max_days": 120,
                "quality_score": 88,
                "harvest_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "certifications": ["Grass-Fed", "Cultured"]
            },
            "Flour": {
                "quantity": "50g",
                "sourced": "Local Mill",
                "days_fresh": 60,
                "max_days": 180,
                "quality_score": 86,
                "harvest_date": (datetime.now() - timedelta(days=45)).strftime("%Y-%m-%d"),
                "certifications": ["Organic", "Stone-Ground"]
            }
        }
    }
}

def get_freshness_status(days_fresh, max_days):
    """Determine freshness status based on days remaining"""
    freshness_ratio = days_fresh / max_days
    if freshness_ratio >= 0.7:
        return "Excellent", "🟢"
    elif freshness_ratio >= 0.4:
        return "Good", "🟡"
    elif freshness_ratio >= 0.2:
        return "Fair", "🟠"
    else:
        return "Poor", "🔴"

def create_freshness_gauge(quality_score):
    """Create a gauge chart for quality score"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=quality_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Quality Score"},
        delta={'reference': 80},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "#f8d7da"},
                {'range': [50, 75], 'color': "#fff3cd"},
                {'range': [75, 90], 'color': "#cfe2ff"},
                {'range': [90, 100], 'color': "#d4edda"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig.update_layout(height=300, font={'size': 12})
    return fig

def create_ingredient_freshness_chart(ingredients):
    """Create a bar chart showing freshness across ingredients"""
    data = []
    for ing_name, ing_data in ingredients.items():
        freshness_pct = (ing_data['days_fresh'] / ing_data['max_days']) * 100
        data.append({
            'Ingredient': ing_name,
            'Freshness %': freshness_pct,
            'Quality': ing_data['quality_score']
        })

    df = pd.DataFrame(data)
    fig = px.bar(df, x='Ingredient', y='Freshness %',
                 color='Quality', color_continuous_scale='RdYlGn',
                 title="Ingredient Freshness & Quality Overview",
                 labels={'Freshness %': 'Days Fresh (%)', 'Quality': 'Quality Score'})
    fig.update_layout(height=400, xaxis_tickangle=-45)
    return fig

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🥗 Fresh & Fair")
    st.markdown("**Complete Food Transparency at Your Fingertips**")
with col2:
    st.metric("Restaurant Rating", "4.8/5", "+0.2")

st.markdown("---")

# Sidebar filters
st.sidebar.header("🔍 Filters")
quality_filter = st.sidebar.slider("Minimum Quality Score", 0, 100, 80)
freshness_priority = st.sidebar.select_slider(
    "Show me ingredients...",
    options=["Excellent", "Good or Better", "Any"]
)

# Main content
st.header("📋 Our Menu")

# Filter menu items
filtered_menu = {}
for dish, data in MENU_DATA.items():
    # Check if all ingredients meet quality threshold
    if all(ing['quality_score'] >= quality_filter for ing in data['ingredients'].values()):
        filtered_menu[dish] = data

if not filtered_menu:
    st.warning(f"No dishes meet your quality requirements (≥{quality_filter}). Adjusting filter...")
    filtered_menu = MENU_DATA

# Display menu items
for dish_name, dish_data in filtered_menu.items():
    with st.expander(f"🍽️ **{dish_name}** - {dish_data['price']}", expanded=False):
        col1, col2 = st.columns([2, 1])

        with col1:
            # Freshness and quality chart
            st.plotly_chart(create_ingredient_freshness_chart(dish_data['ingredients']), use_container_width=True)

        with col2:
            # Overall dish quality metrics
            avg_quality = sum(ing['quality_score'] for ing in dish_data['ingredients'].values()) / len(dish_data['ingredients'])
            st.markdown(f"<div class='metric-box'><h4>Overall Quality</h4><h2>{avg_quality:.0f}/100</h2></div>", unsafe_allow_html=True)

            # Count of excellent ingredients
            excellent_count = sum(1 for ing in dish_data['ingredients'].values() if ing['quality_score'] >= 90)
            st.markdown(f"<div class='metric-box'><h4>Premium Ingredients</h4><h2>{excellent_count}/{len(dish_data['ingredients'])}</h2></div>", unsafe_allow_html=True)

        st.markdown("#### 📦 Ingredient Details")

        # Create ingredient details table
        ing_details = []
        for ing_name, ing_info in dish_data['ingredients'].items():
            status, emoji = get_freshness_status(ing_info['days_fresh'], ing_info['max_days'])
            freshness_pct = (ing_info['days_fresh'] / ing_info['max_days']) * 100

            ing_details.append({
                '✓': emoji,
                'Ingredient': ing_name,
                'Qty': ing_info['quantity'],
                'Source': ing_info['sourced'],
                'Fresh': f"{ing_info['days_fresh']}/{ing_info['max_days']} days",
                'Quality': f"{ing_info['quality_score']}/100",
                'Status': status
            })

        df_ingredients = pd.DataFrame(ing_details)
        st.dataframe(df_ingredients, use_container_width=True, hide_index=True)

        # Detailed ingredient view
        st.markdown("#### 🔍 Detailed Ingredient Analysis")

        cols = st.columns(len(dish_data['ingredients']))
        for idx, (ing_name, ing_info) in enumerate(dish_data['ingredients'].items()):
            with cols[idx]:
                status, emoji = get_freshness_status(ing_info['days_fresh'], ing_info['max_days'])

                if status == "Excellent":
                    css_class = "freshness-excellent"
                elif status == "Good":
                    css_class = "freshness-good"
                elif status == "Fair":
                    css_class = "freshness-fair"
                else:
                    css_class = "freshness-poor"

                html_content = f"""
                <div class='{css_class}'>
                    <h4>{ing_name}</h4>
                    <p><strong>Status:</strong> {emoji} {status}</p>
                    <p><strong>Source:</strong> {ing_info['sourced']}</p>
                    <p><strong>Harvest:</strong> {ing_info['harvest_date']}</p>
                    <p><strong>Days Fresh:</strong> {ing_info['days_fresh']}/{ing_info['max_days']}</p>
                    <p><strong>Quality:</strong> {ing_info['quality_score']}/100</p>
                    <p><strong>Certifications:</strong> {', '.join(ing_info['certifications'])}</p>
                </div>
                """
                st.markdown(html_content, unsafe_allow_html=True)

# Footer with call to action
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("📱 Place Order", use_container_width=True)
with col2:
    st.button("💬 Ask about origin", use_container_width=True)
with col3:
    st.button("📊 See nutrition info", use_container_width=True)

st.markdown("""
<div style='text-align: center; padding: 20px; color: #666;'>
    <p>🌱 <strong>Fresh & Fair</strong> - Bringing complete transparency to food sourcing</p>
    <p>Track every ingredient from farm to table. Quality you can trust.</p>
</div>
""", unsafe_allow_html=True)
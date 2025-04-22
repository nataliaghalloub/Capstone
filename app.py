import streamlit as st
import streamlit.components.v1 as components

# ---------------- Setup ----------------
st.set_page_config(page_title="Masa Madre Forecast App", layout="wide")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Select a Page",
    ["Introduction", "KPI Dashboard", "Forecast Dashboard", "Strategic Recommendations"]
)

# ---------------- Page 1: Introduction ----------------
if page == "Introduction":
    st.image("logo.jpg", width=150)

    st.title("🥖 Data-Driven Business Plan for Masa Madre")
    st.markdown("""
    Welcome to **Masa Madre's Forecasting Tool**  
    This app helps the bakery and its partners make better product and sales decisions by combining data insights with artisan baking values.
    """)

    st.markdown("---")

    st.header("👩‍🍳 About Masa Madre")
    st.markdown("""
    Masa Madre is a sourdough bakery based in **Batroun, Lebanon**, born in 2019 out of a passion for real, artisanal, and sustainable bread.

    We are known for:
    - A **“Why Not?”** baking mindset  
    - Merging global ingredients with traditional recipes  
    - Producing over **10,000 loaves/month**  
    - A product lineup of **70+ varieties**  
    - Educating the community through baking experiences  
    """)

    st.image("sourdough.png", caption="Freshly baked sourdough loaves at Masa Madre", use_column_width=True)

    st.header("🌾 What is Sourdough Bread?")
    st.markdown("""
    Sourdough is naturally fermented using wild yeast. This process:
    - Breaks down gluten  
    - Enhances flavor and crust  
    - Improves nutritional value  

    It’s a more digestible and authentic alternative to industrial bread.
    """)

    st.header("✨ How We Stand Out")
    st.markdown("""
    Masa Madre is more than a bakery — it’s a creative kitchen:
    - Sourcing unique ingredients from around the world  
    - Reimagining classics through bold experimentation  
    - Listening closely to our community and innovating constantly  
    """)

    st.image("babka.png", caption="Decadent chocolate babka — one of our most iconic items", use_column_width=True)
    st.markdown("""
    Our babka reflects the balance of tradition and innovation that defines the Masa Madre approach.
    """)

    st.markdown("""
    ---
    🔮 This app is part of our journey to make data-driven baking decisions while staying true to who we are.
    """)

# ---------------- Page 2: KPI Dashboard ----------------
# Page 2: KPI Dashboard
elif page == "KPI Dashboard":
    st.title("📊 Masa Madre KPI Dashboard")
    st.markdown("Explore the live KPIs and product insights below:")

    st.markdown("### Embedded Tableau Dashboard:")
    components.iframe(
    "https://public.tableau.com/views/CapstoneProjectDashboard_17444077393160/FullDashboard?:embed=y&:display_count=yes&:showVizHome=no",
    height=1700,
    width=1200
    )

# ---------------- Page 3: Forecast Dashboard ----------------
elif page == "Forecast Dashboard":
    st.title("📈 Masa Madre Forecast Dashboard")
    st.markdown("This section shows forecasted sales trends generated using the Meta-Learner model.")

    # 📊 Embed Tableau Forecast Dashboard
    st.markdown("### 📊 Interactive Forecast Visualization")
    st.markdown("_Below is the embedded Tableau dashboard displaying the 12-month forecast._")

    import streamlit.components.v1 as components
    components.iframe(
        "https://public.tableau.com/views/CapstoneProjectDashboard-Forecast/ForecastDashboard?:embed=y&:display_count=yes&:showVizHome=no",
        height=800,
        width=1000
    )

    # 📝 Summary text
    st.markdown("""
    ### 🔍 Insights:
    - This forecast helps visualize expected monthly sales based on historical trends.
    - It combines predictions from Linear Regression, Gradient Boosting, Prophet, and KNN using a Meta-Learner ensemble.
    - The forecast supports production planning, staffing, and promotional decisions.

    _Note: Forecast accuracy depends on the quality and coverage of the historical data._
    """)

# ---------------- Page 4: Strategic Recommendations ----------------
elif page == "Strategic Recommendations":
    st.title("🎯 Strategic Recommendations")
    st.markdown("These data-backed recommendations are designed to support Masa Madre’s strategic planning in sales, production, and client engagement.")

    st.markdown("## 🧍 Client Strategy")
    st.markdown("""
    - **Focus efforts on supermarkets and upscale cafés**, which generate the majority of revenue. Offer them tiered pricing and consistent supply availability.
    - **Expand beyond Beirut and Batroun** to under-tapped areas like **Tripoli, Saida, and Sour**, where no current clients exist despite strong urban demand.
    - **Reactivate dormant clients** with tailored emails featuring reorder reminders, special offers, or previews of new products.
    - **Segment clients by business type and volume** to personalize communication, delivery timing, and minimum order policies.
    """)

    st.markdown("## 🍞 Product Portfolio Actions")
    st.markdown("""
    - **Prioritize high-performing items:**
        - _Plain Loaf_ should remain central to the product catalog due to its exceptional performance in both units and revenue, _Bake Rolls_ comes second.
        - _Babka_ is a key premium product—despite lower volume, it delivers strong margins and should be part of holiday or café-focused promotions.
        - _Whole Wheat Loaf_ also performed consistently and should remain part of the regular offering.
    - **Reduce or redesign low-contribution items:**
        - Products like _Grissini_ should be bundled, offered in seasonal combos, or eventually phased out if profitability doesn’t improve.
    - **Implement a 3-tiered catalog strategy:**
        - **Standard Line**: Plain Loaf, Bake Rolls – optimized for wholesale & supermarket demand.
        - **Premium Line**: Babka, Cakes – for gifting, cafés, and higher-margin segments.
        - **Limited Editions**: Launch seasonal or experimental products for short runs to drive excitement and test new concepts.
    """)

    st.markdown("## 📦 Forecast-Based Operational Planning")
    st.markdown("""
    - **Adopt forecast-based production planning** to adjust baking schedules, staffing, and purchasing in line with projected demand.
    - **Use demand forecasts to prep high-usage ingredients** ahead of time—especially during known spikes (e.g., December holiday season).
    - **Align marketing with forecasted demand**, for example, promoting _Winter Babka Boxes_ or enriched dough items when demand is projected to peak.
    - **Use order size categories (small/medium/large)** to guide delivery prioritization, packaging prep, and batching logistics.
    """)

    st.markdown("## 📊 Business Intelligence & Dashboard Use")
    st.markdown("""
    - **Maintain and regularly update the Streamlit dashboard** as an internal tool for reviewing sales trends and client activity.
    - **Train the team on interpreting dashboard data** to support decision-making without needing external data experts.
    - **Add Customer Lifetime Value (CLV) tracking** to identify which clients are worth prioritizing for long-term retention.
    """)

    st.success("These recommendations aim to guide smart growth, reduce inefficiencies, and support strategic decision-making at Masa Madre.")

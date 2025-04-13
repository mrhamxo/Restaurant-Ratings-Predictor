import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load models and scalers
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/rf_grid_model.pkl")

# Streamlit app layout setup
st.set_page_config(page_title="Restaurant Rating Predictor", layout="wide", page_icon="🍽️")
st.title("🍽️ Restaurant Rating Predictor")
st.markdown("""
This AI-powered app predicts a restaurant's expected rating based on features like pricing, online services, and popularity. 
Ideal for restaurant owners or analysts evaluating customer feedback potential.
""")

st.divider()

# Sidebar for input
st.sidebar.header("📊 Input Restaurant Details")
average_cost = st.sidebar.number_input(
    "Estimated average cost for two (in local currency)", 
    min_value=50, max_value=999999, value=1000, step=200
)

table_booking = st.sidebar.selectbox("Table booking available?", ["Yes", "No"])
online_delivery = st.sidebar.selectbox("Online delivery available?", ["Yes", "No"])
price_range = st.sidebar.selectbox("Price Range (1 = Cheap to 4 = Expensive)", [1, 2, 3, 4])
votes = st.sidebar.number_input("Total number of user votes", min_value=0, max_value=100000, value=100, step=10)

predict_button = st.sidebar.button("Predict Rating 🔢")

# Convert categorical inputs
booking_status = 1 if table_booking == "Yes" else 0 
delivery_status = 1 if online_delivery == "Yes" else 0 

# Input transformation
# Match the exact column names used when fitting the scaler
columns = ['Average Cost for two', 'Has Table booking', 'Has Online delivery', 'Price range', 'Votes']
input_data = pd.DataFrame([[average_cost, booking_status, delivery_status, price_range, votes]], columns=columns)

# Now scale using the DataFrame
scaled_input = scaler.transform(input_data)


# Prediction and Output
if predict_button:
    prediction = model.predict(scaled_input)[0]  # Get scalar value
    rating = round(prediction, 2)

    st.success(f"Predicted Aggregate Rating: **{rating} / 5.0**")

    # Review Classifier
    if rating < 2.5:
        review_class = "📉 Poor"
        color = "#ff4d4d"
    elif rating < 3.5:
        review_class = "🔄 Average"
        color = "#ffa64d"
    elif rating < 4.0:
        review_class = "📊 Good"
        color = "#ffd633"
    elif rating < 4.5:
        review_class = "📈 Very Good"
        color = "#b3ff66"
    else:
        review_class = "📈 Excellent"
        color = "#66ff66"

    st.markdown(f"""
    <div style='padding: 1em; background-color: {color}; border-radius: 10px; text-align: center;'>
        <h3 style='margin: 0;'>Review Category: {review_class}</h3>
    </div>
    """, unsafe_allow_html=True)

    # Add insights
    st.info("*Tip: Increase your votes and online presence to potentially improve perceived ratings.*")

# Add a footer with custom styling
st.markdown("---", unsafe_allow_html=True)

footer = """
<style>
.footer {
    position: relative;
    left: 0;
    bottom: 0;
    width: 100%;
    padding: 15px 0;
    background-color: #f0f2f6;
    text-align: center;
    font-size: 14px;
    color: #555;
}
.footer a {
    margin: 0 10px;
    text-decoration: none;
    color: #555;
}
.footer a:hover {
    color: #000;
}
.footer-icons {
    margin-top: 8px;
}
</style>

<div class="footer">
    <div>Developed with ❤️ by Muhammad Hamza | Powered by Machine Learning | © 2025</div>
    <div class="footer-icons">
        <a href="https://github.com/mrhamxo" target="_blank" title="GitHub">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub" width="24">
        </a>
        <a href="https://www.linkedin.com/in/muhammad-hamza-khattak" target="_blank" title="LinkedIn">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="24">
        </a>
    </div>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)

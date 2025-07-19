# Streamlit App for Salary Prediction (Custom UI)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Salary Predictor", layout="centered")

# Custom CSS for background, title, input fields, and footer
st.markdown('''
    <style>
        html, body, .stApp {
            background: linear-gradient(120deg, #a1c4fd, #c2e9fb);
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center !important;
            font-size: 42px;
            font-weight: bold;
            color: #003366;
        }
        /* Peach background for input widgets */
        .stSelectbox, .stNumberInput, .stTextInput, .stSlider {
            background-color: #ffe5b4 !important;
            border-radius: 10px;
            padding: 10px;
        }
        /* Footer */
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 14px;
            color: #000000;
            text-align: center;
            line-height: 1.4;
        }
    </style>
    <div class="footer">
        <div>Himanshi</div>
        <div>INTERNSHIP_17465167156819baeb7bffe</div>
    </div>
''', unsafe_allow_html=True)

# Title
st.markdown("""
<h1>💼 Employee AI Salary Predictor</h1>
""", unsafe_allow_html=True)

st.subheader("Predict your salary based on your role and background")

# Input fields
education = st.selectbox("📚 Education", ["Bachelor's", "Master's", "PhD"])
gender = st.selectbox("👤 Gender", ["Male", "Female", "Other"])
workclass = st.selectbox("🏢 Workclass", ["Private", "Self-Employed", "Government"])
age = st.slider("🎂 Age", 18, 65, 30)
country = st.selectbox("🌍 Country", ["United States", "India", "Germany", "Canada", "Other"])
role = st.selectbox("💻 Job Role", [
    "Software Engineer",
    "AI Engineer",
    "Data Analyst",
    "Website Handler",
    "ML Engineer",
    "Cloud Engineer"
])

# Fake mapping for demonstration
base_salary = {
    "Software Engineer": 75000,
    "AI Engineer": 95000,
    "Data Analyst": 70000,
    "Website Handler": 65000,
    "ML Engineer": 90000,
    "Cloud Engineer": 85000
}

# Predict
if st.button("🔮 Predict Salary"):
    # Add some variability with age and education
    edu_boost = {"Bachelor's": 5000, "Master's": 10000, "PhD": 15000}
    gender_factor = 0 if gender == "Male" else -1000
    country_boost = 3000 if country == "United States" else 0

    predicted_salary = base_salary[role] + edu_boost[education] + country_boost + gender_factor + (age - 30) * 200
    salary_range = f"${int(predicted_salary - 5000)} - ${int(predicted_salary + 5000)}"

    st.success(f"💰 Estimated Salary Range: {salary_range}")


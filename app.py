import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("wine_quality_model.pkl")

st.title("Wine Quality Predictor")

# Input fields
fixed_acidity = st.number_input("Fixed Acidity", 0.0, 15.0, 7.0)
volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.5)
citric_acid = st.number_input("Citric Acid", 0.0, 1.0, 0.3)
residual_sugar = st.number_input("Residual Sugar", 0.0, 15.0, 2.0)
chlorides = st.number_input("Chlorides", 0.0, 0.5, 0.05)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", 0, 100, 15)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", 0, 300, 46)
density = st.number_input("Density", 0.990, 1.010, 0.996)
pH = st.number_input("pH", 2.5, 4.5, 3.2)
sulphates = st.number_input("Sulphates", 0.0, 2.0, 0.5)
alcohol = st.number_input("Alcohol", 8.0, 15.0, 10.0)
type_val = st.selectbox("Type", ["Red", "White"])
type_encoded = 0 if type_val == "Red" else 1

if st.button("Predict Quality"):
    features = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                          chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                          pH, sulphates, alcohol, type_encoded]])
    prediction = model.predict(features)
    st.success(f"Predicted Wine Quality: **{prediction[0].capitalize()}**")



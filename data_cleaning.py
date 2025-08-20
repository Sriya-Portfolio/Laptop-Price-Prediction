# data_cleaning.py
import streamlit as st
import re

def data_cleaning_page():
    st.header("🧹 Data Cleaning and Preprocessing")

    st.write("""
    ### Why Data Cleaning for Manual Calculation?
    Although we use a manual formula, data cleaning ensures:
    - Correct and complete inputs (e.g., proper resolution format).
    - Accurate feature engineering (e.g., calculating PPI from resolution).
    - Handling unrealistic values (e.g., negative storage sizes).

    Let's demonstrate some essential data validation steps below.
    """)

    # User Inputs for Demonstration
    resolution = st.text_input("Enter Resolution (e.g., 1920x1080):")
    ram = st.number_input("Enter RAM (GB):", min_value=1, max_value=128, step=1)
    ssd = st.number_input("Enter SSD (GB):", min_value=0, max_value=2000, step=50)

    if st.button("Validate Inputs"):
        # Resolution Validation
        if not re.match(r'^\d+x\d+$', resolution):
            st.error("Invalid resolution format! Use widthxheight (e.g., 1920x1080).")
        else:
            st.success("Resolution format is correct.")

        # RAM Validation
        if ram < 1 or ram > 128:
            st.error("Invalid RAM size. Please enter a value between 1 and 128 GB.")
        else:
            st.success(f"RAM: {ram} GB is valid.")

        # SSD Validation
        if ssd < 0 or ssd > 2000:
            st.error("Invalid SSD size. Enter a value between 0 and 2000 GB.")
        else:
            st.success(f"SSD: {ssd} GB is valid.")

    # Feature Engineering Example: Calculate PPI from Resolution
    st.subheader("🖥️ Feature Engineering: Calculating PPI (Pixels Per Inch)")

    screen_size = st.number_input("Enter Screen Size (inches):", min_value=10.0, max_value=20.0, step=0.1)
    if resolution and screen_size:
        try:
            width, height = map(int, resolution.lower().split('x'))
            ppi = ((width**2 + height**2) ** 0.5) / screen_size
            st.success(f"Calculated PPI: {ppi:.2f}")
        except Exception as e:
            st.error("Error calculating PPI. Check your inputs.")
    else:
        st.warning("Enter resolution and screen size to calculate PPI.")

    st.write("""
    ### Summary:
    - ✅ Proper input validation prevents incorrect predictions.  
    - ✅ Simple feature engineering (e.g., PPI) enhances formula accuracy.  
    - ✅ Manual calculation remains effective when inputs are clean and validated.  
    """)

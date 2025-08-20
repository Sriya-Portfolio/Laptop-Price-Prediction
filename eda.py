# eda.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def eda_page():
    st.header("📊 Exploratory Data Analysis (EDA)")

    st.write("""
    ### Why EDA for Manual Calculation?
    Although our project uses a manual formula, EDA helps us understand:
    - **Which features impact laptop prices most.**
    - **How specifications like RAM, brand, and display affect pricing trends.**
    - **Validating our manual price calculation logic.**

    We can use hypothetical or sample data to demonstrate these trends.
    """)

    # Sample Data for Demonstration
    sample_data = pd.DataFrame({
        'Company': ['Dell', 'HP', 'Apple', 'Asus', 'Acer'],
        'Average Price (INR)': [60000, 55000, 150000, 65000, 45000],
        'Average RAM (GB)': [8, 8, 16, 12, 8]
    })

    # Bar Chart: Average Price by Company
    st.subheader("💻 Average Laptop Price by Brand")
    fig, ax = plt.subplots()
    sns.barplot(x='Company', y='Average Price (INR)', data=sample_data, palette='coolwarm', ax=ax)
    ax.set_ylabel("Average Price (INR)")
    ax.set_xlabel("Company")
    ax.set_title("Average Price by Brand")
    st.pyplot(fig)

    # Line Chart: RAM vs. Price Trend (Demonstrating Linear Relation)
    st.subheader("💾 RAM vs. Price Trend (Why RAM Matters)")
    ram_price = pd.DataFrame({
        'RAM (GB)': [4, 8, 16, 32, 64],
        'Price (INR)': [25000, 40000, 70000, 120000, 180000]
    })
    st.line_chart(ram_price.set_index('RAM (GB)'))

    # Explanation: Impact of Features
    st.write("""
    ### Insights from EDA:
    - **Brands like Apple** have a significantly higher price due to premium hardware and brand value.  
    - **RAM and SSD** strongly influence price because they directly impact performance.  
    - **Display features** (e.g., IPS, Touchscreen) add extra cost.  

    These insights directly shape our manual pricing formula. 📊
    """)

# abstract.py
import streamlit as st

def abstract_page():
    st.header("📜 Project Abstract")
    st.write("""
    This project is a **Laptop Price Prediction System** with user and admin management. 
    The application allows users to input laptop specifications and receive an estimated price using a custom calculation method.
    
    ### Objectives:
    - Provide users with accurate price estimates based on specifications.
    - Enable secure user registration and login.
    - Allow admins to manage users and view prediction histories.
    
    ### Features:
    - Multi-page Streamlit Application
    - MySQL Database for User Management
    - Custom Price Calculation Model
    """)

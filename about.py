# about.py
import streamlit as st

def about_page():
    st.header("ℹ️ About the Project")

    # Project Overview
    st.subheader("📌 Project Overview")
    st.write("""
    This project is a **Laptop Price Prediction System** built using Streamlit. 
    The application estimates laptop prices based on user-selected configurations 
    such as brand, model, RAM, CPU, GPU, and other components. 
    It aims to assist users in understanding price variations and 
    making informed purchase decisions.
    """)

    st.image("Assets/Images/HP laptop.png", caption="Laptop Prediction - HP Laptop", use_container_width=True)

    # Motivation
    st.subheader("💡 Motivation")
    st.write("""
    The laptop market offers numerous models with varying specifications and prices. 
    However, determining whether a laptop is priced fairly based on its features 
    can be challenging for buyers. 
    This project aims to:
    - Provide accurate price estimates for different configurations.  
    - Help users compare the value of various brands and models.  
    - Educate users about the factors that influence laptop prices.  
    """)

    st.image("Assets/Images/market insights.png", caption="Laptop Market Insights", use_container_width=True)

    # Technology Stack
    st.subheader("🛠️ Technology Stack")
    st.write("""
    - **Frontend:** Streamlit (Python)  
      A fast and easy-to-use framework for building interactive web applications.  
    - **Backend:** Manual Formula-Based Price Calculation  
      Prices are computed using a custom formula based on real market component values.  
    - **Database:** MySQL  
      Used to store user inputs and maintain a history of predictions.  
    - **Hosting:** Streamlit Cloud / Local Server  
      The application is deployed and accessible via a web interface.  
    """)

    st.image("Assets/Images/technology-stack.png", caption="Technology Stack", use_container_width=True)

    # Key Features
    st.subheader("✨ Key Features")
    st.write("""
    - 📊 **Interactive Interface:** Users can easily input their desired specifications.  
    - 📈 **Real-Time Price Calculation:** Instant results based on selected configurations.  
    - 📝 **Detailed Component Breakdown:** Explanation of price components (CPU, GPU, etc.).  
    - 📂 **Prediction History:** Users can view and compare previous estimates.  
    """)

    # Impact
    st.subheader("🌍 Impact and Benefits")
    st.write("""
    This project benefits a wide range of users, including:
    - 🧑‍💻 **Tech Enthusiasts:** Compare laptops based on specifications and cost.  
    - 🛒 **Buyers:** Make informed purchase decisions with estimated fair prices.  
    - 📈 **Retailers:** Offer competitive pricing and transparency to customers.  
    """)

    # Conclusion
    st.subheader("🔚 Conclusion")
    st.write("""
    The **Laptop Price Prediction System** bridges the gap between technical specifications 
    and real-world costs. It empowers users to make confident purchasing decisions 
    and better understand the value behind each feature.  
    """)

    st.success("💻 Get started by exploring the features or predicting your laptop price!")

# price_prediction.py
import streamlit as st

def price_prediction_page():
    st.header("💰 Laptop Price Prediction")

    # Market Prices for Components
    cpu_prices = {
        "Intel i3": 5000,
        "Intel i5": 10000,
        "Intel i7": 15000,
        "AMD Ryzen 5": 12000,
        "AMD Ryzen 7": 17000,
        "Other": 8000,
    }

    gpu_prices = {
        "Intel Integrated": 3000,
        "NVIDIA": 15000,
        "AMD": 12000,
        "Other": 5000,
    }

    os_prices = {
        "Windows": 8000,
        "MacOS": 20000,
        "Linux": 3000,
        "Other": 1000,
    }

    # ✅ Updated Company Prices (Base cost for brands)
    company_prices = {
        "Dell": 5000,
        "HP": 4500,
        "Apple": 20000,
        "Asus": 4000,
        "Lenovo": 14500,
        "Acer": 3800,
        "MSI": 7000,
        "Samsung": 5500,
        "LG": 5200,
        "Microsoft": 8000,
        "Other": 3000,
    }

    # Collect Inputs
    company = st.selectbox(
        "Company", 
        ["Dell", "HP", "Apple", "Asus", "Lenovo", "Acer", "MSI", "Samsung", "LG", "Microsoft", "Other"]
    )

    # Company-specific Laptop Models
    if company == "Dell":
        model = st.selectbox("Model", ["Inspiron", "XPS", "Latitude", "Vostro", "Alienware", "G Series", "Precision"])
    elif company == "HP":
        model = st.selectbox("Model", ["Pavilion", "Spectre", "Envy", "Omen", "Victus", "EliteBook", "ProBook"])
    elif company == "Apple":
        model = st.selectbox("Model", ["MacBook Air", "MacBook Pro"])
    elif company == "Asus":
        model = st.selectbox("Model", ["Vivobook", "Zenbook", "ROG", "TUF", "ProArt"])
    elif company == "Lenovo":
        model = st.selectbox("Model", ["ThinkPad", "Legion", "IdeaPad", "Yoga", "Slim", "LOQ"])
    elif company == "Acer":
        model = st.selectbox("Model", ["Aspire", "Nitro", "Predator", "Swift", "Spin", "TravelMate"])
    elif company == "MSI":
        model = st.selectbox("Model", ["Stealth", "Raider", "Vector", "Pulse", "Creator", "Prestige"])
    elif company == "Samsung":
        model = st.selectbox("Model", ["Galaxy Book", "Notebook", "Odyssey"])
    elif company == "LG":
        model = st.selectbox("Model", ["Gram", "Ultra PC"])
    elif company == "Microsoft":
        model = st.selectbox("Model", ["Surface Laptop", "Surface Book", "Surface Pro"])
    elif company == "Other":
        model = st.text_input("Enter Model Name")

    # Other Inputs
    ram = st.slider("RAM (GB)", 4, 64, step=4)
    weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)
    touchscreen = st.radio("Touchscreen", ["Yes", "No"])
    ips = st.radio("IPS Display", ["Yes", "No"])
    screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1)
    resolution = st.text_input("Resolution (e.g., 1920x1080)")
    cpu = st.selectbox("CPU", list(cpu_prices.keys()))
    hdd = st.number_input("HDD (GB)", min_value=0, max_value=2000, step=100)
    ssd = st.number_input("SSD (GB)", min_value=0, max_value=2000, step=100)
    gpu = st.selectbox("GPU", list(gpu_prices.keys()))
    os = st.selectbox("Operating System", list(os_prices.keys()))

    if st.button("Predict Price"):
        try:
            x_res, y_res = map(int, resolution.lower().replace('x', ' ').split())
            ppi = ((x_res**2 + y_res**2) ** 0.5) / screen_size
        except:
            st.error("Invalid resolution format. Use widthxheight (e.g., 1920x1080).")
            return

        # Convert Categorical Inputs
        touchscreen_value = 1500 if touchscreen == "Yes" else 0
        ips_value = 1000 if ips == "Yes" else 0

        # Component Prices from Market Values
        cpu_value = cpu_prices[cpu]
        gpu_value = gpu_prices[gpu]
        os_value = os_prices[os]

        # ✅ FIXED: Use company instead of model for company base price
        company_value = company_prices.get(company, 3000)

        # Manual Calculation Based on Market Prices
        price_inr = (
            company_value +
            (ram * 500) - 
            (weight * 200) + 
            touchscreen_value + 
            ips_value + 
            (ppi * 50) + 
            (hdd * 5) + 
            (ssd * 10) +
            cpu_value + 
            gpu_value + 
            os_value
        )

        st.success(f"Estimated Laptop Price: ₹{price_inr:.2f}")

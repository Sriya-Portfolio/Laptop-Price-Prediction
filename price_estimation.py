import streamlit as st

def price_estimation_page():
    st.header("💻💰 Price Estimations")

    st.markdown("""

    To provide a more accurate laptop price prediction, it's essential to incorporate realistic market values for each component. Below is an updated breakdown of typical component prices in India as of 2025:

    ### 1. **RAM (Random Access Memory):**
    - **4 GB:** ₹1,500 – ₹2,000
    - **8 GB:** ₹3,000 – ₹4,000
    - **16 GB:** ₹6,000 – ₹8,000
    - **32 GB:** ₹12,000 – ₹15,000
    - **64 GB:** ₹24,000 – ₹30,000

    ### 2. **Storage:**
    - **HDD (Hard Disk Drive):**
    - **1 TB:** ₹3,000 – ₹4,000
    - **2 TB:** ₹5,000 – ₹6,500
    - **SSD (Solid State Drive):**
    - **256 GB:** ₹3,500 – ₹4,500
    - **512 GB:** ₹6,000 – ₹7,500
    - **1 TB:** ₹10,000 – ₹12,000

    ### 3. **CPU (Processor):**
    - **Intel:**
    - **i3:** ₹8,000 – ₹10,000
    - **i5:** ₹15,000 – ₹18,000
    - **i7:** ₹25,000 – ₹30,000
    - **AMD Ryzen:**
    - **Ryzen 5:** ₹12,000 – ₹15,000
    - **Ryzen 7:** ₹20,000 – ₹25,000

    ### 4. **GPU (Graphics Processing Unit):**
    - **Integrated Graphics:** Typically included with the CPU; minimal additional cost.
    - **Dedicated Graphics:**
    - **NVIDIA GeForce GTX/RTX Series:** ₹15,000 – ₹50,000 (depending on the model)
    - **AMD Radeon Series:** ₹10,000 – ₹40,000 (depending on the model)

    ### 5. **Display:**
    - **Standard Display:** Included in base laptop price.
    - **Touchscreen Feature:** Adds approximately ₹5,000 – ₹7,000.
    - **IPS Panel:** Adds approximately ₹3,000 – ₹5,000.

    ### 6. **Brand Premium:**
    - **Apple:** Significant premium; laptops often start above ₹1,00,000.
    - **Dell/HP/Lenovo:** Mid-range premium; laptops range from ₹40,000 to ₹1,50,000.
    - **Asus/Acer:** Generally more affordable; laptops range from ₹30,000 to ₹1,00,000.

    ### 7. **Operating System:**
    - **Windows 11 Home:** Typically included in the laptop price.
    - **Windows 11 Pro:** Adds approximately ₹5,000 – ₹7,000.
    - **macOS:** Exclusive to Apple devices; included in the premium.
    - **Linux/Other:** Often free or minimal cost.

    ### 8. **Additional Features:**
    - **Weight Reduction (e.g., ultra-thin designs):** Can add ₹5,000 – ₹10,000.
    - **High PPI (Pixels Per Inch) Displays:** Higher resolution screens can add ₹5,000 – ₹15,000.

    ### **Revised Price Estimation Formula:**

    To estimate the laptop price more accurately:

    1. **Base Price:** Start with a base price of ₹20,000.
    2. **Add Component Costs:** Sum the costs of selected components (RAM, Storage, CPU, GPU, Display features).
    3. **Add Brand Premium:** Factor in the brand's typical pricing.
    4. **Add Operating System Cost:** If applicable.
    5. **Add Additional Features Cost:** For features like lightweight design or high-resolution displays.

    **Example Calculation:**

    For a laptop with the following specifications:
    - **Brand:** Dell
    - **RAM:** 16 GB
    - **Storage:** 512 GB SSD
    - **CPU:** Intel i5
    - **GPU:** NVIDIA GeForce GTX 1650
    - **Display:** 15.6" with IPS panel
    - **Touchscreen:** No
    - **Operating System:** Windows 11 Home

    **Estimated Price:**
    - **Base Price:** ₹20,000
    - **RAM (16 GB):** ₹7,000
    - **Storage (512 GB SSD):** ₹7,000
    - **CPU (Intel i5):** ₹16,000
    - **GPU (NVIDIA GTX 1650):** ₹20,000
    - **Display (IPS Panel):** ₹4,000
    - **Brand Premium (Dell):** ₹20,000
    - **Operating System (Windows 11 Home):** Included

    **Total Estimated Price:** ₹94,000

    """)

    st.info("""
    
    ### 📈 **Price Formula**  
    **Price** = 300 + (RAM × 50) − (Weight × 10) + (Touchscreen × 150) + (IPS × 100)  
         + (PPI × 2) + (HDD × 0.8) + (SSD × 1.2) + CPU Value + GPU Value + Company Value + OS Value

    """)

    st.success("*Note: These prices are approximate and can vary based on specific models, configurations, and market fluctuations.*")

    st.markdown("""
        
    By incorporating these realistic component prices and brand premiums, your laptop price prediction model will provide estimates that closely align with the current market in India. 

    """)
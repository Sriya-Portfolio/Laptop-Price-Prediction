# dataset.py
import streamlit as st
import pandas as pd

def dataset_page():
    # Page Title
    st.header("📂 Dataset and Manual Calculation Approach")

    # Detailed Explanation
    st.markdown("""
    ## 📝 Why Dataset Is Important for Manual Calculation:
    In this project, instead of using machine learning models, we rely on a **manual calculation formula** to predict laptop prices. 
    However, having a dataset is still crucial because it helps us:
    - **Understand Pricing Patterns:** Analyze how laptop features impact prices.
    - **Build an Accurate Formula:** Develop a manual formula based on real-world trends.
    - **Validate Predictions:** Compare formula outputs to actual prices from the dataset.

    ## 🚀 Why Manual Calculation Is More Important than ML:
    In this project, manual calculation is the best approach because:
    - **Predictability:** Laptop prices follow clear patterns based on specifications.
    - **Transparency:** Our formula is explainable and easy to adjust.
    - **No Overfitting:** Manual formulas are not sensitive to small datasets.
    - **Easy Updates:** Quickly adjust the formula for new trends without retraining.

    ## 🧮 Manual Calculation Formula (Example):
    Based on our dataset analysis, we derived this formula:

    **Price (INR) = Base Price (Brand) + (CPU Multiplier × CPU Score) + (RAM × ₹1500) + (SSD × ₹10) + (Screen Size × ₹1000) + (PPI Factor) + (GPU Factor)**

    ### 📝 Explanation of Formula Components:
    - **Base Price (Brand):** Premium brands like Apple have a higher starting cost.  
    - **CPU Multiplier:** Higher benchmark scores (e.g., PassMark) indicate better performance and cost more.  
    - **RAM (₹1500/GB):** Each additional GB of RAM increases the cost.  
    - **SSD (₹10/GB):** Each additional GB of SSD adds a cost increment.  
    - **Screen Size (₹1000/inch):** Larger screens have a higher price.  
    - **PPI Factor:** Higher resolution displays increase price.  
    - **GPU Factor:** Dedicated graphics cards significantly raise prices.  

    ---

    ## 📊 Key Factors Affecting Laptop Prices:
    | **Factor**         | **Impact on Price**                                         |
    |---------------------|------------------------------------------------------------|
    | 💻 **Brand**        | Apple, Dell XPS, and Razer have higher base prices.       |
    | 🧠 **Processor**    | Newer and faster CPUs increase cost (Intel i9 > i7 > i5). |
    | 🧩 **RAM & Storage**| More RAM and SSD capacity raise the cost.                |
    | 📺 **Display**      | Higher resolution and size increase the price.            |
    | 🎮 **Graphics Card**| Dedicated GPUs (e.g., NVIDIA RTX) increase the cost.     |
    | 🔋 **Battery Life** | Long battery life models have premium components.         |

    ---

    ## 🧠 Why Manual Calculation Is More Suitable than ML:
    | Aspect                | Manual Calculation                   | Machine Learning                   |
    |-----------------------|-------------------------------------|------------------------------------|
    | **Accuracy**          | High (Due to domain knowledge)     | Depends on training quality       |
    | **Transparency**      | Fully Explainable                  | Opaque (Black-box models)         |
    | **Adaptability**      | Easy to modify formula             | Needs retraining for changes      |
    | **Data Needs**        | Low                                | High (Large datasets required)    |
    | **Overfitting Risk**  | None                               | Possible in small datasets        |
    
    🚀 **Conclusion:**  
    - A carefully designed manual formula based on real-world pricing patterns can outperform ML models.  
    - Manual calculation is efficient, cost-effective, and adaptable for real-world use cases.  
    """)

    # Example Dataset Display
    st.subheader("📊 Sample Laptop Dataset for Manual Calculation")

    # Sample Data for Display
    sample_data = pd.DataFrame({
        'Brand': ['Apple', 'Dell', 'HP', 'Asus', 'Acer'],
        'Processor': ['M1', 'Intel i7', 'Ryzen 5', 'Intel i5', 'Ryzen 3'],
        'CPU Score': [10000, 9000, 8000, 7500, 6000],
        'RAM (GB)': [16, 16, 8, 12, 8],
        'SSD (GB)': [512, 512, 256, 512, 256],
        'Screen Size (inches)': [13.3, 15.6, 14, 15.6, 14],
        'Resolution': ['2560x1600', '1920x1080', '1920x1080', '1920x1080', '1366x768'],
        'GPU': ['Integrated', 'NVIDIA GTX 1650', 'Integrated', 'NVIDIA GTX 1650', 'Integrated'],
        'Actual Price (INR)': [150000, 85000, 60000, 75000, 45000]
    })

    # Display Sample Dataset
    st.dataframe(sample_data)

    # Additional Insights
    st.markdown("""
    ## 🧠 Insights from the Dataset:
    - **Brand Impact:** Apple laptops have a significantly higher base price.  
    - **CPU Impact:** Intel i7 models cost more than i5 and Ryzen 5 models.  
    - **RAM and SSD Impact:** More RAM and SSD lead to linear price increases.  
    - **GPU Impact:** Laptops with NVIDIA GTX 1650 are more expensive than integrated graphics models.  

    ## 📌 Key Observations for Formula Development:
    - 🏷️ **Brand:** Apple models have a higher base price.  
    - ⚙️ **CPU:** Higher PassMark scores indicate more expensive processors.  
    - 💾 **RAM/SSD:** Prices increase linearly with storage and memory.  
    - 📺 **Screen:** Larger screen sizes and higher resolutions increase cost.  
    - 🎮 **GPU:** Dedicated graphics cards add significant cost.  
    """)

    # Summary Note
    st.success("""
    🚀 This dataset and analysis guide us to create an accurate **manual price calculation formula** 
    that is interpretable, transparent, and reliable without relying on machine learning models.
    """)


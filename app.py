import streamlit as st
from abstract import abstract_page
from about import about_page
from dataset import dataset_page
from eda import eda_page
from data_cleaning import data_cleaning_page
from price_estimation import price_estimation_page
from price_prediction import price_prediction_page
from conclusion import conclusion_page

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Sidebar
st.title('💻 Laptop Price Prediction Using Streamlit: A Machine Learning Model for Estimating Laptop Prices Based on Features 💻')

# --- Initialize session state ---
if 'page' not in st.session_state:
    st.session_state.page = "abstract"

# --- Sidebar Navigation with Active Page Highlight ---
with st.sidebar:
    st.sidebar.title("📑 Pages")
    pages = [
        ("📄 Abstract", "abstract"),
        ("ℹ️ About", "about"),
        ("📊 Dataset", "dataset"),
        ("📈 EDA", "eda"),
        ("🧹 Data Cleaning", "data_cleaning"),
        (" 💻💰 Price Estimation", "price_estimation"),
        ("💰 Price Prediction", "price_prediction"),
        ("🤝 Conclusion", "conclusion")
    ]

    # CSS for Active Page Styling
    st.markdown(
        """
        <style>
            div.stButton > button {
                width: 100%;
                padding: 10px;
                font-weight: bold;
                border-radius: 10px;
                margin-bottom: 8px;
                border: 2px solid transparent;
                transition: all 0.2s;
            }
            .active-btn button {
                background-color: #f0f8ff; /* Light Blue Background */
                border: 2px solid #87CEFA; /* Sky Blue Border */
                box-shadow: 0px 0px 12px rgba(135, 206, 250, 0.5);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display Sidebar Buttons
    for label, page_id in pages:
        button_key = f"{page_id}_btn"

        # Highlight Active Button
        if st.session_state.page == page_id:
            st.markdown('<div class="active-btn">', unsafe_allow_html=True)
            if st.button(label, key=button_key, use_container_width=True):
                st.session_state.page = page_id
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button(label, key=button_key, use_container_width=True):
                st.session_state.page = page_id

# --- Page Routing ---
if st.session_state.page == 'abstract':
    abstract_page()
elif st.session_state.page == 'about':
    about_page()
elif st.session_state.page == 'dataset':
    dataset_page()
elif st.session_state.page == 'eda':
    eda_page()
elif st.session_state.page == 'data_cleaning':
    data_cleaning_page()
elif st.session_state.page == 'price_estimation':
    price_estimation_page()
elif st.session_state.page == 'price_prediction':
    price_prediction_page()
elif st.session_state.page == 'conclusion':
    conclusion_page()
import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Financial Forecasting",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎉 Welcome to Financial Forecasting")

st.markdown(
    """
        <style>
            [data-testid="stSidebar"] {
                background-color: #F6CF68; 
            }
            [data-testid="stSidebar"] * {
                color: black;
            }
            .stApp {
            background-color: #626262;
        }
    
        /* Title text color */
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }
    
        /* Uploaded file box text */
        .css-1cpxqw2, .css-1d391kg {
            color: white !important;
        }
        </style>
    """,
    unsafe_allow_html=True
)

# Logic
# Just instruction to use this web app
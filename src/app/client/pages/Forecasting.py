import streamlit as st

# Page config
st.title("Forecasting")

st.sidebar.title("Metrics")
st.sidebar.radio(
    "Choose one metric you want to forecast",
    ('ROA', 'ROE', 'Value_add', 'Revenue', 'EBITDA')
)
st.sidebar.markdown(
    """
    <div style="height:50vh;"></div>
    """,
    unsafe_allow_html=True
)

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


uploaded_file = st.file_uploader(
    "Please upload your excel data file here",
    type=["xlsx", "xls"],
    accept_multiple_files=False
)

predict_button = st.button("Predict", icon="📈")

# Page logic
if predict_button:
    if uploaded_file is None:
        st.error("❌ No file uploaded. Please upload an Excel file.")
    else:
        df = pd.read_excel(uploaded_file)
        st.success("Predicting...")

        st.write("### 🔍 Result:")
        # Insert logic of prediction here
        st.write("Prediction completed. ")
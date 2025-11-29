import streamlit as st


# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Financial Forecasting",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Metric")
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


# -----------------------------------------------------
# CUSTOM CSS FOR THEMING & LAYOUT
# -----------------------------------------------------

st.markdown(
"""
    <style>
        [data-testid="stSidebar"] {
            background-color: #F3BA2F; 
        }
        [data-testid="stSidebar"] * {
            color: black;
        }
        .stApp {
        background-color: #1E1E1E;
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

st.title("Financial Forecasting")

uploaded_file = st.file_uploader(
    "Please upload your excel data file here",
    type=["xlsx", "xls"],
    accept_multiple_files=False
)

predict_button = st.button("Predict", icon="📈")

# --- Logic: only show result after clicking Predict ---
if predict_button:
    if uploaded_file is None:
        st.error("❌ No file uploaded. Please upload an Excel file.")
    else:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("✅ File uploaded successfully! Running prediction...")

            # Placeholder for actual prediction logic
            # result = model.predict(df)

            st.write("### 🔍 Result:")
            st.write("Prediction completed. (Insert your model output here.)")

        except Exception as e:
            st.error(f"⚠️ Error reading the file: {e}")
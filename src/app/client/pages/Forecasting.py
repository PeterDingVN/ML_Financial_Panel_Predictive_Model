import streamlit as st
from src.app.server import *

# Page config
st.title("Forecasting")

st.sidebar.title("Metrics")
metric = st.sidebar.radio(
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
    
    div.stAlert p {
        color: #ffffff !important;
        font-weight: 200;
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
status = st.empty()
if predict_button:
    if uploaded_file is None:
        st.error("❌ No file uploaded. Please upload an Excel file.")
    else:
        # Phase 1: data verification
        status.success("Checking data...")
        req_col = col_list(metric)
        df = translation(pd.read_excel(uploaded_file))

        ## Case when data input is cleaned
        if all(col in df.columns for col in req_col):
            # ensure correct col order
            df = df[req_col]

        ## Case when users input original data scraped from FiinProX
        else:
            try:
                df = col_trans(uploaded_file)
                df = df[req_col]

        ## Case other than those cases (irrelevant or wrong formatted data)
            except Exception:
                status.empty()
                st.error(f"Please make sure your data start at A1, or else, not intervened since download from FiinProX"
                         f"and check your data columns if they match required col: {req_col}. "
                         f"For variable meaning checkout data/var_definition.txt")

        ## check for null
        if df.isna().sum().sum():
            st.error("Input data contains missing values, please fill the data or drop the entire row")

        status.empty()
        st.success(f"{df.columns}, {df.head()}")



        # # Phase 2: pred making using models
        # status.success("Predicting...")
        # ## Set index for company, year -> keep the id while only inputing features into model
        # df = df.set_index(['company', 'year'])
        #
        #
        # # Phase 3: return result
        #
        # status.empty()
        # st.write("### 🔍 Result:")
        # # Insert logic of prediction here
        # st.write(f"Prediction completed: {metric}")
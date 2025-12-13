import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Financial Forecasting",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎉 Welcome to Financial Forecasting 🎉")

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

# ... your existing code for the title ...
# st.title("🎉 Welcome to Financial Forecasting 🎉")

# 1. Introduction Text


# 2. Warning Block (Using st.warning makes it stand out visually)

st.write("""
**Data preparation:**
- Please make sure your data is the very raw data taken from FiinProX, and to be sure, just take more data columns
than needed for error-free run
- Else, please make sure data columns follow naming rule. You can check this by upload a random data, and the system
will raise error plus give you recommnedation on all needed columns, and their according names.
""")

# 3. Contact Info with Links
# Replace the URL strings below with your actual profile links
linkedin_link = "https://www.linkedin.com/in/%C4%91inh-thanh-th%E1%BA%BF-peter-ding-855b1a281"
github_link = "https://github.com/PeterDingVN"

st.markdown(f"""
If you have any comment on improvement, feel free to contact me via [Linkedin]({linkedin_link}) or follow me on [Github]({github_link}).
""")

st.markdown("🤩 Now go to **Forecasting** and enjoy!")

st.warning("""
**Remember:**
- Data trained is from 2015 to 2023 only.
- Imbalance exists, so prediction for some particular companies in OTC, PRIVATE might not be so good. For details, check out `\\doc\\pred_list.txt`.
""")

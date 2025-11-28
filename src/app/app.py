import streamlit as st

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Financial Forecasting",
    page_icon="💵",
    layout="wide"
)

st.sidebar.title("Metric")

st.sidebar.markdown(
    """
    <div style="height:50vh;"></div>
        }
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <img src="https://streamlit.io/images/brand/streamlit-mark-color.png"
             style="width:100px; margin-bottom:0px;">
        <p style="font-size:12px; margin-top:0;">Powered by Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------------------------------
# CUSTOM CSS FOR THEMING & LAYOUT
# -----------------------------------------------------
st.markdown("""
<style>

.stApp {
    background-color: #950606;
}

/* RIGHT COLUMN BACKGROUND */

.right-column {
    padding: 25px;
    border-radius: 8px;
}

/* Bring right content closer to the left */
.tight-layout {
    margin-left: -80px;     /* pull right panel toward left */
}

/* Button Styling */
.stButton>button {
    background-color: #0b6e4f;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    border: none;
}
.stButton>button:hover {
    background-color: #0f8a64;
}

/* Output / Error Box */
.result-box {
    border: 3px solid white;
    padding: 20px;
    border-radius: 10px;
    background-color: #ffd8c2;
    min-height: 150px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# TITLE
# -----------------------------------------------------
st.markdown(
    "<h1 style='text-align: center;'>💲 FINANCIAL FORECASTING 💲</h1>",
    unsafe_allow_html=True
)
# -----------------------------------------------------
# MAIN LAYOUT (LEFT & RIGHT)
# -----------------------------------------------------
right = st.columns(1)

# -----------------------------------------------------
# LEFT AREA
# -----------------------------------------------------
# with left:
#     st.markdown('<div class="left-column">', unsafe_allow_html=True)
#
#     st.subheader("Streamlit Logo")
#     st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
#
#     st.subheader("Metrics")
#     metrics = ["ROA", "ROE", "EBITDA", "Value_add", "Revenue"]
#
#     selected_metric = st.radio(
#         "Select a metric to predict:",
#         metrics,
#         index=None
#     )
#
#     st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------
# RIGHT AREA
# -----------------------------------------------------
with right:
    st.markdown('<div class="right-column tight-layout">', unsafe_allow_html=True)

    st.subheader("Upload Excel File")
    uploaded_file = st.file_uploader("Upload your .xlsx file", type=["xlsx"])

    predict_btn = st.button("Predict")

    st.subheader("Output")
    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    # # Prediction logic
    # if predict_btn:
    #     if uploaded_file is None:
    #         st.error("❌ Please upload an Excel (*.xlsx) file before predicting.")
    #     elif selected_metric is None:
    #         st.error("❌ Please choose ONE metric before predicting.")
    #     else:
    #         st.success(f"✔ Prediction completed for **{selected_metric}**")
    #         st.write("📌 (Model results will appear here.)")
    # else:
    #     st.info("Awaiting input... Upload file and choose metric.")

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# import leafmap.foliumap as leafmap
#
# st.set_page_config(layout="wide")
#
# # Customize the sidebar
# markdown = """
# A Streamlit map template
# <https://github.com/opengeos/streamlit-map-template>
# """
#
# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# st.sidebar.image(logo)
#
# # Customize page title
# st.title("Streamlit for Geospatial Applications")
#
# st.markdown(
#     """
#     This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/opengeos/streamlit-map-template).
#     """
# )
#
# st.header("Instructions")
#
# markdown = """
# 1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
# 2. Customize the sidebar by changing the sidebar text and logo in each Python files.
# 3. Find your favorite emoji from https://emojipedia.org.
# 4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.
#
# """
#
# st.markdown(markdown)
#
# m = leafmap.Map(minimap_control=True)
# m.add_basemap("OpenTopoMap")
# m.to_streamlit(height=500)
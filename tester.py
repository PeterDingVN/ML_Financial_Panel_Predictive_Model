import subprocess
import os

# Folder where THIS file is located (ML_Financial_Panel_Predictive_Model/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the path to app.py inside src/app/
APP_PATH = os.path.join(BASE_DIR, "src", "app", "app.py")

# Launch Streamlit
subprocess.run(["streamlit", "run", APP_PATH])
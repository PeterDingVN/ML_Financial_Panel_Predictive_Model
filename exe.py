import subprocess
import os
import sys

# Folder where THIS file is located (ML_Financial_Panel_Predictive_Model/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the path to client.py inside src/app/
APP_PATH = os.path.join(BASE_DIR, "src", "app", "client", "Homepage.py")

# Launch Streamlit
subprocess.run([sys.executable, "-m", "streamlit", "run", APP_PATH])
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


img_path = "/apps/tue.png"

st.set_page_config(
    page_title="Tabular Data Anonymization App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.roko.com/help',
        'Report a bug': "https://www.roko.com/bug",
        'About': "This is a low-code image classification app !"
    }
)

# st.write("Hello there!, Welcome to the Data Anonymization and Privacy application")
st.title("🔌 Data Anonymization & Privacy app")
image = Image.open(img_path)
st.sidebar.image(image)

"""
We're very excited to release `Data Anonymization & privacy app`, which makes it easy for the researcher to run data anonymization on their data with ease.

Just drop the dataset you have and select the models you want to run and let the magic happen
"""

lottie_url = "https://lottie.host/522e60e3-6834-4fc5-b4eb-1a6930e973b1/NoZS1aEm55.json"
st_lottie(lottie_url, key="user", height=500, width=500, loop=True, )

st.title("What's included")

"""
- Anonymize specific tabular columns using algorithms such as k-anonymity,..
- Replace Personally identifiable information (PII) with pseudorandom data 
- Encrypt group of columns with hashlibs


"""
st.divider()
st.info("This is the 1.0 version of the Data Anonymization app.", icon="ℹ️")

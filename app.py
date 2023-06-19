import streamlit as st
from spare_parts import *


st.set_page_config(page_title="Cab  Management", page_icon="🚗", layout="wide", initial_sidebar_state="expanded")
st.image("https://www.pccwebworld.com/images/cab-management-system.jpg", width=700)

with st.sidebar:
    #st.title("Bike Rental Prediction")

    st.header = "Navigation"
    button_1 = st.radio("Select Operations", ['Driver', "Cab","Management"])

    # inserting one image here
    st.image("data:image/jpeg;base64,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", width=300)


if(button_1):
    if(button_1 == "Driver"):
        driver_app()
        
    if(button_1 == "Cab"):
        cab_app()
    if(button_1 == "Management"):
        managment()


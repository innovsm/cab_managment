import streamlit as st
from spare_parts import *

with st.sidebar:
    #st.title("Bike Rental Prediction")
    button_1 = st.radio("page", ['Driver', "Cab","Management"])


if(button_1):
    if(button_1 == "Driver"):
        driver_app()
        
    if(button_1 == "Cab"):
        cab_app()
    if(button_1 == "Management"):
        managment()


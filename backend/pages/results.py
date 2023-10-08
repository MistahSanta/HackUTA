from __init__ import st_text_display
import streamlit as st

def getResults():
    bestCrop = "None"
    with open("bestCrops.txt", "r") as file:
        bestCrop = file.read() 

    st.write("The best crop is: " + bestCrop)
    st_text_display()
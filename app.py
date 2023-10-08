import streamlit as st


st.title("Crop Recommendation Predictor")



input1 = st.text_input("Amount of Nitrogen (kg/ha)", placeholder="Min:0, Max:100")
input2 = st.text_input("Amount of Phosphorus (kg/ha)", placeholder="Min:0, Max:100")
input3 = st.text_input("Amount of Potassium (kg/ha)", placeholder="Min:0, Max:100")
input4 = st.number_input("Average Temperature (in Celsius) during growing period", placeholder="Min:0, Max:100")
input5 = st.number_input("Average Relative Humidity (in %) during growing period", placeholder="Min:0, Max:100", min_value=0.0, max_value=100.0)
input6 = st.number_input("Soil pH during growing period", placeholder="Min:0, Max:100", min_value=0.0, max_value=14.0)
input7 = st.text_input("Amount of Rainfall (in mm) received during growing period", placeholder="Min:0, Max:100")


if st.button("Submit"):
   
    st.write("Input 1 (Nitrogen):", input1)
    st.write("Input 2 (Phosphorus):", input2)
    st.write("Input 3 (Potassium):", input3)
    st.write("Input 4 (Temperature):", input4)
    st.write("Input 5 (Relative Humidity):", input5)
    st.write("Input 6 (Soil pH):", input6)
    st.write("Input 7 (Rainfall):", input7)
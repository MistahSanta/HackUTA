import streamlit as st 
from model import recommendCrop

def surveyDisplay(): 
    st.title("Crop Recommendation Predictor")

    amountNitrogen = int ( st.number_input("Amount of Nitrogen (kg/ha)", placeholder="Min:0, Max:100") )
    amountPhos = int ( st.number_input("Amount of Phosphorus (kg/ha)", placeholder="Min:0, Max:100") )
    amountPotas = int ( st.number_input("Amount of Potassium (kg/ha)", placeholder="Min:0, Max:100") )
    avgTemp = float ( st.number_input("Average Temperature (in Celsius) during growing period", placeholder="Min:0, Max:100") )
    avgHumid = float ( st.number_input("Average Relative Humidity (in %) during growing period", placeholder="Min:0, Max:100", min_value=0.0, max_value=100.0) )
    pH = float ( st.number_input("Soil pH during growing period", placeholder="Min:0, Max:100", min_value=0.0, max_value=14.0) )
    amountRainfall = float ( st.number_input("Amount of Rainfall (in mm) received during growing period", placeholder="Min:0, Max:100") )

    if st.button("Submit"):
        st.write("Based off your soil, to maximum yield use: " + str(recommendCrop( amountNitrogen, amountPhos, amountPotas, amountRainfall, avgHumid, avgTemp, pH ))) 


    

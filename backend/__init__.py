import streamlit.components.v1 as components
from pages.survey import surveyDisplay
from notification import sendNotification

# try: 
#     r = sendNotification('Crops need watering!')
# except Exception as e:
#     print(e) 

#surveyDisplay()


_component_func = components.declare_component(
    "CropSurvey",
    url="http://localhost:3000", # fetch front end component
)

def st_text_display():
    component_value = _component_func()
    return component_value





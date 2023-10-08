import os 
import requests 
from dotenv import load_dotenv

# load environment variable 
load_dotenv()

USER_ID = os.environ.get('PUSHOVER_USER_KEY')
API_TOKEN = os.environ.get('PUSHOVER_API_KEY')

    
def sendNotification(text):
   
    payload = {"message": text, 
               "user": USER_ID, 
               "token": API_TOKEN }
    
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload)
    return r

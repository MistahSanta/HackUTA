
import streamlit as st 
import pandas as pd 

from model import top_n_recommendation

df = pd.DataFrame( {
    'crop': top_n_recommendation['label'],
    'similiarity': top_n_recommendation['similiarity']
})





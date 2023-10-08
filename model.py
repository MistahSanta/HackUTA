
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing as pre
import numpy as np 


sample_size = 1760

# Read the csv data
df = pd.read_csv('data/cropData.csv', encoding='latin-1', sep=',')

print(df.head())

# Get the minimum and maximum parameter of each data 
max_df = df.max()
min_df = df.min()

scaler = MinMaxScaler()

df[ ['N','P','K','temperature','humidity','ph','rainfall']] = scaler.fit_transform(df[ ['N','P','K','temperature','humidity','ph','rainfall']])



farmer_Example = {
    'N' : 90,
    'P' : 40,
    'K' : 45,
    'temperature': 20.89,
    'humidity' : 82,
    'ph' : 7.50232,
    'rainfall': 202.294354,
    
}

farmer_example_scaled = {
    key: (farmer_Example[key] - min_df[key]) / ( max_df[key] - min_df[key])
    for key in farmer_Example.keys()
}

item_features = df[ ['N','P','K','temperature','humidity','ph','rainfall']]
crop_features = pd.Series(farmer_example_scaled).values.reshape(1,-1)
similiar_scores = cosine_similarity( item_features, crop_features)


df['similiarity'] = similiar_scores


recommended_crops = df.sort_values(by='similiarity', ascending=False)


top_n_recommendation = recommended_crops[['label', 'similiarity']].head(5)

print( top_n_recommendation)
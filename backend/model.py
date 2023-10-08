
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing as pre
import numpy as np 


def recommendCrop(amountNitrogen , amountPhos, amountPotas, amountRainfall, avgHumid, avgTemp, pH):
    # Read the csv data
    df = pd.read_csv('..//data/cropData.csv', encoding='latin-1', sep=',')
    
    # Get the minimum and maximum parameter of each data 
    max_df = df.max()
    min_df = df.min()

    scaler = MinMaxScaler()
    threshold = 0.90

    df[ ['N','P','K','temperature','humidity','ph','rainfall']] = scaler.fit_transform(df[ ['N','P','K','temperature','humidity','ph','rainfall']])

    farmer_Example = {
        'N' : amountNitrogen,
        'P' : amountPhos,
        'K' : amountPotas,
        'temperature': avgTemp,
        'humidity' : avgHumid,
        'ph' : pH,
        'rainfall': amountRainfall,
        
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


    top_n_recommendation = recommended_crops[['label', 'similiarity']]

    
    top_n_recommendation = top_n_recommendation.drop_duplicates(subset="label", keep='first')
    
    top_n_recommendation = top_n_recommendation[top_n_recommendation['similiarity'] > threshold].head(3)
    
    with open("bestCrops.txt", "w") as file:
        file.write( top_n_recommendation.head(1) )
    return top_n_recommendation['label'].to_string(index=False)

import pandas as pd
import numpy as np
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
#-----------------------------------------------------------------------------------------------
#Tourist Attraction Dataset
data_Attraction = pd.read_excel('Baguio_Dataset_Version2.xlsx', sheet_name='Tourist Attraction')
data_Attraction_selected = data_Attraction[['Place_ID','Name','Category']]
#-----------------------------------------------------------------------------------------------
#Restaurant
data_restaurant = pd.read_excel('Baguio_Dataset_Version2.xlsx', sheet_name='Restaurant')
data_restaurant_selected = data_restaurant[['Restaurant_ID','Name','Cuisine Type']]
#-----------------------------------------------------------------------------------------------
#For Training a model and getting recommendation system
class recommendation_model:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
    def fit(self,places,categories):
        self.places = places
        self.categories = categories
        #Train the model to make cosine similarity with the help of vectorizer
        self.tfidf_matrix = self.vectorizer.fit_transform(categories)
        #It calculates the cosine similarity between all category vectors
        self.cosine_sim = cosine_similarity(self.tfidf_matrix)
    def get_recommendation(self,place_index,n_recommendation = 5):
        target_category = self.categories[place_index]
        sim_scores = []
        #places_index it should be the index of the places
        #Only include items with matching categories
        #It doesnt include the target
        for idx, category in enumerate(self.categories):
            if category == target_category and idx != place_index:
                sim_scores.append((idx, self.cosine_sim[place_index][idx]))
                
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[:n_recommendation]
        item_indices = [i[0] for i in sim_scores]
        return self.places[item_indices]
    
#-----------------------------------------------------------------------------------------------
#Train the two model
"""
Notes in this code:
index of the places when the user interact to the place it returns the index number of the place
"""
#Tourist Attraction
Tourist = recommendation_model()
Tourist.fit(data_Attraction_selected['Name'],data_Attraction_selected['Category'])
#Restaurant Recommendation
Restaurant = recommendation_model()
Restaurant.fit(data_restaurant_selected['Name'],data_restaurant_selected['Cuisine Type'])
target = 3
sample = list(Restaurant.get_recommendation(target))
print(sample)

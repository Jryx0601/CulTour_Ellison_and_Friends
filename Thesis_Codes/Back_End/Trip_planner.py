"""
Planning in Trip Planning:
1. Based on user interest like the Category
2. trip generating 2 restaurant and 3 visits can be based on the user interest 

Alternative Version:
1. The user pick of the category like two or more on Tourist and Restaurant
2. trip generating 2 restaurant with position like [Tour,Tour,Restau,Tour,Tour,Restau]
- 2-3 main attractions/activities
- 2-3 restaurants (1 lunch, 1 dinner, optional breakfast spot)
"""


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#-----------------------------------------------------------------------------------------------
#Tourist Attraction Dataset
data_Attraction = pd.read_excel('Baguio_Dataset_Version2.xlsx', sheet_name='Tourist Attraction')
data_Attraction_selected = data_Attraction[['Place_ID','Name','Category']]
#-----------------------------------------------------------------------------------------------
#Restaurant
data_restaurant = pd.read_excel('Baguio_Dataset_Version2.xlsx', sheet_name='Restaurant')
data_restaurant_selected = data_restaurant[['Restaurant_ID','Name','Cuisine Type']]

class trip_planner_generator:
    def __init__(self,target,categories):
        self.target = target
        self.categories = categories 
    def category_finder(self,n_recommendation = 3):
        places = []
        #idx is the index number of the categories in order to find the name
        for idx,values in enumerate(self.categories):
            if self.target == values:
                places.append(data_Attraction_selected['Name'][idx])

        return places[:n_recommendation]
    

#sample implementation
target = 'Nature'
Tourist = trip_planner_generator(target,data_Attraction_selected['Category'])
sample = Tourist.category_finder()
print(sample)
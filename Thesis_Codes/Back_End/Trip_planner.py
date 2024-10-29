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
    def category_finder(self,type,n_recommendation):
        places = []
        #idx is the index number of the categories in order to find the name
        for idx,values in enumerate(self.categories):
            if self.target == values and type == 'Tourist':
                places.append(data_Attraction_selected['Name'][idx])
            elif self.target == values and type == 'Restaurant':
                places.append(data_restaurant_selected['Name'][idx])

        return places[:n_recommendation]
    
def trip_planner(tourist_Attaraction,Restaurant):
    pattern = ['Attraction','Attraction','Restaurant','Attraction','Restaurant']
    place_generated = []


    Tourist_Attraction_Number = 0
    Restaurant_Number = 0
    for x in range(len(pattern)):
        if pattern[x] == 'Attraction' and Tourist_Attraction_Number < len(tourist_Attaraction):
            place_generated.append(tourist_Attaraction[Tourist_Attraction_Number])
            Tourist_Attraction_Number += 1
        elif pattern[x] == 'Restaurant' and Restaurant_Number < len(Restaurant):
            place_generated.append(Restaurant[Restaurant_Number])
            Restaurant_Number += 1
    return place_generated

            

#sample implementation
#User input 
target_tourist = 'Nature'
target_Restaurant = 'Filipino'

#insert the data
Tourist = trip_planner_generator(target_tourist,data_Attraction_selected['Category'])
Restaurant = trip_planner_generator(target_Restaurant, data_restaurant_selected['Cuisine Type'])

#Insert the number for pattern in trip planner
Tourist_Suggestion = Tourist.category_finder('Tourist',3)
Restaurant_Suggestion = Restaurant.category_finder('Restaurant',2)

#Get the generated place
final_generated = trip_planner(Tourist_Suggestion,Restaurant_Suggestion)
print(final_generated)

"""
Needs for changes:
Pattern when it is limited for data in dataset
"""
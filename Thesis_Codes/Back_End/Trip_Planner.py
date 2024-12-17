import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import choices, sample
from pathlib import Path
script_location_dataset = Path(__file__).parent
dataset_path = script_location_dataset/ 'Baguio_Dataset.xlsx'
#Tourist Attraction Dataset
data_Attraction = pd.read_excel(dataset_path, sheet_name='Tourist Attraction')
data_Attraction_selected = data_Attraction[['Name','Category','Description','Latitude','Longitude','History']]

#Restaurant
data_restaurant = pd.read_excel(dataset_path, sheet_name='Restaurant')
data_restaurant_selected = data_restaurant[['Name','Cuisine Type','Description','Latitude','Longitude']]

class trip_planner_generator:
    def __init__(self,target,categories):
        self.target = target
        self.categories = categories 

    def randomizer_places(self,array,n_recommendation):
        array_final = list(sample(array,k = n_recommendation))
        return array_final

    def category_finder(self,type,n_recommendation):
        places = []
        #idx is the index number of the categories in order to find the name
        #if the name is equal to the value it stores to the places
        for idx,values in enumerate(self.categories):
            if self.target == values and type == 'Tourist':
                if data_Attraction_selected['Name'][idx] not in places:
                    places.append(data_Attraction_selected['Name'][idx])
            elif self.target == values and type == 'Restaurant':
                if data_restaurant_selected['Name'][idx] not in places:
                    places.append(data_restaurant_selected['Name'][idx])

        #Needs to randomize
        places = self.randomizer_places(places,n_recommendation)
        return places
    

def trip_planner(tourist_Attaraction,Restaurant):
    pattern = ['Attraction','Restaurant','Attraction','Restaurant']
    #To get unique value to the list so it doesn't repeat
    tourist_Attaraction = list(set(tourist_Attaraction))
    Restaurant = list(set(Restaurant))

    #This is where it will be generated
    place_generated = []
    Tourist_Attraction_Number = 0
    Restaurant_Number = 0
    for x in range(len(pattern)):
        if pattern[x] == 'Attraction' and Tourist_Attraction_Number < len(tourist_Attaraction):
            if tourist_Attaraction[Tourist_Attraction_Number] not in place_generated:
                place_generated.append(tourist_Attaraction[Tourist_Attraction_Number])
                Tourist_Attraction_Number += 1
            else: continue
        elif pattern[x] == 'Restaurant' and Restaurant_Number < len(Restaurant):
            if Restaurant[Restaurant_Number] not in place_generated:
                place_generated.append(Restaurant[Restaurant_Number])
                Restaurant_Number += 1
            else: continue
    return place_generated

# #sample implementation
# #User input 
target_tourist = 'Art'
target_Restaurant = 'Filipino'

#insert the data
Tourist = trip_planner_generator(target_tourist,data_Attraction_selected['Category'])
Restaurant = trip_planner_generator(target_Restaurant, data_restaurant_selected['Cuisine Type'])

#Insert the number for pattern in trip planner
Tourist_Suggestion = Tourist.category_finder('Tourist',2)
Restaurant_Suggestion = Restaurant.category_finder('Restaurant',2)
#Get the generated place
final_generated = trip_planner(Tourist_Suggestion,Restaurant_Suggestion)
print(final_generated)
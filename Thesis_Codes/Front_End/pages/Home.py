#python -m streamlit run 00_app.py
import streamlit as st
import numpy as np
import pandas as pd
import datetime
from streamlit_folium import st_folium, folium_static
import folium
from pathlib import Path
import os
import sys
import random
from random import choices
st.set_page_config(initial_sidebar_state="collapsed",layout="wide")
#---------------------------------------------------------------
#Accessing a file in back_End
script_recommendation = Path(__file__).parent.parent.parent
sys.path.append(str(script_recommendation))
from Back_End.Recommender_Model import recommendation_model, data_Attraction_selected, data_restaurant_selected
#Tourist Recommendation
Tourist = recommendation_model()
Tourist.fit(data_Attraction_selected['Name'],data_Attraction_selected['Category'])
#Restaurant Recommendation
Restaurant = recommendation_model()
Restaurant.fit(data_restaurant_selected['Name'],data_restaurant_selected['Cuisine Type'])
#---------------------------------------------------------------
#---------------------------------------------------------------
#Turning array into dictionary with index of the places
def places_index_Home(array,type_place):
    place_dictionary = {}
    match type_place:
        case 'Tourist':
            for i in range(len(array)):
                for j in range(len(data_Attraction_selected['Name'])):
                    if array[i] == data_Attraction_selected['Name'][j]:
                        place_dictionary[array[i]] = j
                    else:
                        continue
            return place_dictionary
        case 'Restaurant':
            for i in range(len(array)):
                for j in range(len(data_restaurant_selected['Name'])):
                    if array[i] == data_restaurant_selected['Name'][j]:
                        place_dictionary[array[i]] = j
                    else:
                        continue
            return place_dictionary
    
    

#---------------------------------------------------------------
#pip install streamlit-option-menu
from streamlit_option_menu import option_menu
#st.title("CulTour")
#----------------------------------------------------------------------------------------------------
selected = option_menu(
    menu_title = None,
    options=["Map","Trip Planning","Account"],
    icons=["house","book","person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
if selected == "Map":
    #Display of map
   #Testing lang ito

   #Interactive map
   #https://discuss.streamlit.io/t/interactive-maps-using-geopandas-geodataframe-geodataframe/63706

   #or
   #Folium map
   #pip install streamlit-folium
   #https://github.com/randyzwitch/streamlit-folium
    m = folium.Map(location = [14.3269, 120.9575], zoom_start = 50)
    folium.Marker(
        [14.3269, 120.9575],
        popup = "DLSUD",
        tooltip = "DLSUD"
        ).add_to(m)
   
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width = 1735, height= 725)
    st.divider()

    #Filter 
    options = st.multiselect(
    "Filter",
    ["Restaurant", "Tourist Attraction"])
    st.divider()

   #Images_Place
    script_location = Path(__file__).parent
    sample = 'test1'
    image_path_tourist = script_location/'images'/f'{sample}.jpg'

    #Places_Accessing and randomizing the places
    places_Tourist = list(data_Attraction_selected['Name'])
    places_Tourist_new = list(places_index_Home(places_Tourist,'Tourist').values())
    #Columns of pop over
    st.subheader('Tourist Attraction')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        pass
    with col2:
        pass
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass


#----------------------------------------------------------------------------------------------------
    st.divider()

    script_location_Restaurant = Path(__file__).parent

    if 'random_restaurant_places' not in st.session_state:
        st.session_state.random_restaurant_places = list(choices(data_restaurant_selected['Name'],k=5))


    places_Restaurant = st.session_state.random_restaurant_places
    places_Restaurant_new = list(places_index_Home(places_Restaurant,'Restaurant').values())
    
    if 'Restaurant_data' not in st.session_state:
        st.session_state.Restaurant_data = {} 
    st.subheader('Restaurant')
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        image_path_tourist = script_location/'Restaurant'/f'{data_restaurant_selected['Name'][places_Restaurant_new[0]]}.jpg' or f'{data_restaurant_selected['Name'][places_Restaurant_new[0]]}.jfif' or f'{data_restaurant_selected['Name'][places_Restaurant_new[0]]}.png'
        st.image(str(image_path_tourist),use_column_width=True)
        if st.button(data_restaurant_selected['Name'][places_Restaurant_new[0]]):
            st.session_state.Restaurant_data['Name'] = data_restaurant_selected['Name'][places_Restaurant_new[0]]
            st.session_state.Restaurant_data['Index'] = places_Restaurant_new[0]
            st.session_state.Restaurant_data['Cuisine Type'] = data_restaurant_selected['Cuisine Type'][places_Restaurant_new[0]]
            st.session_state.Restaurant_data['Longitude'] = data_restaurant_selected['Longitude'][places_Restaurant_new[0]]
            st.session_state.Restaurant_data['Latitude'] = data_restaurant_selected['Latitude'][places_Restaurant_new[0]]
            st.switch_page('pages/place_page.py')
    with col2:
        pass
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass

    
#----------------------------------------------------------------------------------------------------
if selected =="Trip Planning":
    st.title("Category")

    options = st.multiselect(
    "Restaurant",
    ["Restaurant", "Tourist Attraction"])

    options1 = st.multiselect(
    "Tourist",
    ["Restaurasnt", "Tourist Attracstion"])

    generated = st.button("Click me")

    st.divider()

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        if generated:
            st.write("generated here")
    
    with col2:
        if generated:
            st.write("generated here")

    with col3:
        if generated:
            st.write("generated here")

    with col4:
        if generated:
            st.write("generated here")

    with col5:
        if generated:
            st.write("generated here")
    

#----------------------------------------------------------------------------------------------------
if selected == "Account":
    piccol, deets = st.columns([2,3])

    with piccol:
        st.title("Account Profile")

    with deets:
        st.write(" ")
        st.subheader("Name")
        st.write("Admin")
        
        st.subheader("Gender")
        gender = st.selectbox("",["Male","Female","Helicopter"])
        st.write("")

        st.subheader("Birthday")
        d = st.date_input("", datetime.date(2002, 2, 6))
        st.write(d)


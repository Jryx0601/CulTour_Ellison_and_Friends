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
from random import choices, sample
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
#----------------------------------------------------------------------------------------------------
# Data of the Tourist Attraction Access
    script_location_Tourist = Path(__file__).parent
    extensions = ['.jpg','.jfif','.png','.gif','.JPG','.jpeg']

    if 'random_tourist_places' not in st.session_state:
        st.session_state.random_tourist_places = list(sample(list(data_Attraction_selected['Name']),k=5))

    places_Tourist = st.session_state.random_tourist_places
    places_Tourist_new = list(places_index_Home(places_Tourist,'Tourist').values())
    
#----------------------------------------------------------------------------------------------------
# Data of the Restaurant Access
    script_location_Restaurant = Path(__file__).parent

    if 'random_restaurant_places' not in st.session_state:
        st.session_state.random_restaurant_places = list(sample(list(data_restaurant_selected['Name']),k=5))

    places_Restaurant = st.session_state.random_restaurant_places
    places_Restaurant_new = list(places_index_Home(places_Restaurant,'Restaurant').values())
#----------------------------------------------------------------------------------------------------

    m = folium.Map(location = [16.41639, 120.59306], zoom_start = 50)
    st.divider()

    #Filter 
    options = st.selectbox(
    "Filtered Map:",
    ["Restaurant", "Tourist Attraction"])

    if options == 'Tourist Attraction':
        coordinates = []
        for i in range(len(places_Tourist_new)):
            folium.Marker(
                [data_Attraction_selected['Latitude'][places_Tourist_new[i]],data_Attraction_selected['Longitude'][places_Tourist_new[i]]],
                tooltip=data_Attraction_selected['Name'][places_Tourist_new[i]],
                popup=data_Attraction_selected['Name'][places_Tourist_new[i]]
            ).add_to(m)

            coordinates.append([data_Attraction_selected['Latitude'][places_Tourist_new[i]],data_Attraction_selected['Longitude'][places_Tourist_new[i]]])

        if coordinates:
            m.fit_bounds(coordinates)

        folium_static(m, width = 1735, height= 725)
    elif options == 'Restaurant':
        coordinates = []
        for i in range(len(places_Tourist_new)):
            folium.Marker(
                [data_restaurant_selected['Latitude'][places_Restaurant_new[i]],data_restaurant_selected['Longitude'][places_Restaurant_new[i]]],
                tooltip=data_restaurant_selected['Name'][places_Restaurant_new[i]],
                popup=data_restaurant_selected['Name'][places_Restaurant_new[i]]
            ).add_to(m)

            coordinates.append([data_restaurant_selected['Latitude'][places_Restaurant_new[i]],data_restaurant_selected['Longitude'][places_Restaurant_new[i]]])

        if coordinates:
            m.fit_bounds(coordinates)
        
        folium_static(m, width = 1735, height= 725)
    st.divider()

#-------------------------------------------------------------------------------------------------------------------------------------
    st.subheader('Tourist Attraction')
    if 'Tourist_data' not in st.session_state:
        st.session_state.Tourist_data = {}

    if 'Tourist_recommendation' not in st.session_state:
        st.session_state.Tourist_recommendation = None


    col1,col2,col3,col4,col5 = st.columns(5)
    cols = [col1,col2,col3,col4,col5]
    for i in range(len(places_Tourist_new)):
        with cols[i]:
            image_path_tourist = script_location_Tourist/ 'Tourist_Attraction'
            for ext in extensions:
                tourist_image = image_path_tourist/f'{data_Attraction_selected['Name'][places_Tourist_new[i]]}{ext}'
                if tourist_image.exists():
                    image_path_tourist = tourist_image
            st.image(str(image_path_tourist),use_column_width=True)
            
            if st.button(data_Attraction_selected['Name'][places_Tourist_new[i]], use_container_width=True):
                st.session_state.Tourist_data['Name'] = data_Attraction_selected['Name'][places_Tourist_new[i]]
                st.session_state.Tourist_data['Index'] = places_Tourist_new[i]
                st.session_state.Tourist_data['Category'] = data_Attraction_selected['Category'][places_Tourist_new[i]]
                st.session_state.Tourist_data['Longitude'] = data_Attraction_selected['Longitude'][places_Tourist_new[i]]
                st.session_state.Tourist_data['Latitude'] = data_Attraction_selected['Latitude'][places_Tourist_new[i]]
                st.session_state.Tourist_data['Description'] = data_Attraction_selected['Description'][places_Tourist_new[i]]

                recommendation_tourist = list(Tourist.get_recommendation(places_Tourist_new[i]))
                st.session_state.Tourist_recommendation = list(places_index_Home(recommendation_tourist,'Tourist').values())
                st.switch_page('pages/tourist_page.py')

#----------------------------------------------------------------------------------------------------
    st.divider()
    if 'Restaurant_data' not in st.session_state:
        st.session_state.Restaurant_data = {} 

    st.subheader('Restaurant')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
 
    for i in range(len(places_Restaurant_new)):
        with cols[i]:
            
            image_path_restaurant = script_location_Restaurant/'Restaurant'
            for ext in extensions:
                restuarant_image = image_path_restaurant/f'{data_restaurant_selected['Name'][places_Restaurant_new[i]]}{ext}'
                if restuarant_image.exists():
                    image_path_tourist = restuarant_image
            st.image(str(image_path_tourist),use_column_width=True)
            if st.button(data_restaurant_selected['Name'][places_Restaurant_new[i]], use_container_width=True):
                st.session_state.Restaurant_data['Name'] = data_restaurant_selected['Name'][places_Restaurant_new[i]]
                st.session_state.Restaurant_data['Index'] = places_Restaurant_new[i]
                st.session_state.Restaurant_data['Cuisine Type'] = data_restaurant_selected['Cuisine Type'][places_Restaurant_new[i]]
                st.session_state.Restaurant_data['Longitude'] = data_restaurant_selected['Longitude'][places_Restaurant_new[i]]
                st.session_state.Restaurant_data['Latitude'] = data_restaurant_selected['Latitude'][places_Restaurant_new[i]]
                st.switch_page('pages/place_page.py')

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


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
    st_data = st_folium(m, width = 725)
    st.divider()

   #Images_Place
    script_location = Path(__file__).parent
    sample = 'test1'
    image_path = script_location/'images'/f'{sample}.jpg'

    #Places_Accessing and randomizing the places
    places_Tourist = list(choices(data_Attraction_selected['Name'],k=5))
    places_Tourist_new = list(places_index_Home(places_Tourist,'Tourist').values())
    print(places_Tourist_new[0])
    #Columns of pop over
    st.subheader('Tourist Attraction')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(str(image_path), use_column_width=True)
        with st.popover(data_Attraction_selected['Name'][places_Tourist_new[0]]):
            place = folium.Map(location = [data_Attraction_selected['Latitude'][places_Tourist_new[0]],data_Attraction_selected['Longitude'][places_Tourist_new[0]]],zoom_start=50)
            folium.Marker(
                [data_Attraction_selected['Latitude'][places_Tourist_new[0]],data_Attraction_selected['Longitude'][places_Tourist_new[0]]],
            popup=data_Attraction_selected['Name'][places_Tourist_new[0]],
            tooltip=data_Attraction_selected['Name'][places_Tourist_new[0]]
            ).add_to(place)

            folium_static(place,width=650,height=500)
            st.title(data_Attraction_selected['Name'][places_Tourist_new[0]])
#------------------------------------------------------------------------------------------------------------
            st.divider()
            st.header('Description')
            st.text(data_Attraction_selected['Description'][places_Tourist_new[0]])
            st.divider()
#------------------------------------------------------------------------------------------------------------
            st.header(f'Recommendation of {data_Attraction_selected['Category'][0]}:')
    with col2:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col3:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col4:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col5:
        with st.popover('Name_Place'):
            st.text('Sample')


#----------------------------------------------------------------------------------------------------
    st.divider()
    st.subheader('Restaurant')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(str(image_path), use_column_width=True)
        with st.popover('Name_Place'):
            st.text('Sample')
    with col2:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col3:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col4:
        with st.popover('Name_Place'):
            st.text('Sample')
    with col5:
        with st.popover('Name_Place'):
            st.text('Sample')

    
#----------------------------------------------------------------------------------------------------
if selected =="Trip Planning":
    st.write("bleh")
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


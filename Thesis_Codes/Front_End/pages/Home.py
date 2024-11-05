#python -m streamlit run 00_app.py
import streamlit as st
import numpy as np
import pandas as pd
import datetime
from streamlit_folium import st_folium
import folium
from pathlib import Path
import os
import sys
st.set_page_config(initial_sidebar_state="collapsed")
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
#pip install streamlit-option-menu
from streamlit_option_menu import option_menu
#st.title("ColTour")
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
    m = folium.Map(location = [14.3269, 120.9575], zoom_start = 16)
    folium.Marker(
        [14.3269, 120.9575],
        popup = "DLSUD",
        tooltip = "DLSUD"
        ).add_to(m)
   
    # call to render Folium map in Streamlit
    st_data = st_folium(m, width = 725)

    st.divider()

   #Places
    script_location = Path(__file__).parent
    sample = 'test1'
    image_path = script_location/'images'/f'{sample}.jpg'
   #Dito pagkaclick ng image lalabas ito
#    with st.popover("Sample"):
#         st.image(str(image_path))
#         st.markdown("Pic ulet dito")
#         st.divider()
#         st.markdown("Place name")
#         st.caption("Description ng place")

#    with st.popover("Image dito"):
#         st.markdown("Pic ulet dito")
#         st.divider()
#         st.markdown("Place name")
#         st.caption("Description ng place")

    st.text('Tourist Attraction')
    #Columns of pop over
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

    st.divider()

    st.text('Restaurant')


    
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
        st.write("Vinz Brian P. Familara")
        
        st.subheader("Gender")
        gender = st.selectbox("",["Male","Female","Helicopter"])
        st.write("")

        st.subheader("Birthday")
        d = st.date_input("", datetime.date(2002, 2, 6))
        st.write(d)


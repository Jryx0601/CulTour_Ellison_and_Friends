#python -m streamlit run 00_app.py
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from streamlit_folium import st_folium
import folium
from pathlib import Path
import os

#pip install streamlit-option-menu
from streamlit_option_menu import option_menu
#st.title("ColTour")


"""
st.image(full directory from drive to the location)
"""
#Menu
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
   #hindi niya mahanap ung pic :(
   script_location = Path(__file__).parent
   image_path = script_location/'images'/'test1.jpg'
   st.image(str(image_path))
   #Dito pagkaclick ng image lalabas ito
   with st.popover("Image dito"):
        st.markdown("Pic ulet dito")
        st.divider()
        st.markdown("Place name")
        st.caption("Description ng place")

   with st.popover("Image dito"):
        st.markdown("Pic ulet dito")
        st.divider()
        st.markdown("Place name")
        st.caption("Description ng place")

    

if selected =="Trip Planning":
    st.write("bleh")

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


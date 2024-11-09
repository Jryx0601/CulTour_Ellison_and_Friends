import streamlit as st
import folium
from streamlit_folium import folium_static

if 'Restaurant_data' in st.session_state:
    if st.button('Back'):
        st.switch_page('pages/Home.py')
    st.header(st.session_state.Restaurant_data['Name'])
    st.divider()
    place = folium.Map(location = [st.session_state.Restaurant_data['Latitude'],st.session_state.Restaurant_data['Longitude']], zoom_start=50)
    folium.Marker(
        [st.session_state.Restaurant_data['Latitude'],st.session_state.Restaurant_data['Longitude']],
        popup=st.session_state.Restaurant_data['Name'],
        tooltip=st.session_state.Restaurant_data['Name']
    ).add_to(place)

    folium_static(place, width = 1735, height= 725)
    st.header(f'Cuisine Type: {st.session_state.Restaurant_data['Cuisine Type']}')
    st.divider()
    st.header(f'Similar You Might Like: ')
    col1,col2,col3,col4,col5 = st.columns(5)

    
    


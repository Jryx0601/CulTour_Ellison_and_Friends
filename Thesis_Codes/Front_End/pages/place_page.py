import streamlit as st
import folium
from streamlit_folium import folium_static
from pathlib import Path
import sys

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

    st.subheader('Description: ')
    st.subheader(st.session_state.Restaurant_data['Description'])
    st.header(f'Cuisine Type: {st.session_state.Restaurant_data['Cuisine Type']}')
    st.divider()

if 'Restaurant_Recommendation' in st.session_state:

    script_recommendation = Path(__file__).parent.parent.parent
    sys.path.append(str(script_recommendation))
    from Back_End.Recommender_Model import data_restaurant_selected

    script_location = Path(__file__).parent
    extensions = ['.jpg','.jfif','.png','.gif','.JPG','.jpeg']
    st.header(f'Similar You Might Like: ')
    col1,col2,col3,col4,col5 = st.columns(5)
    cols = [col1,col2,col3,col4,col5]

    for i in range(len(st.session_state.Restaurant_Recommendation)):
        with cols[i]:
            image_path = script_location/'Restaurant'
            for ext in extensions:
                image_path_restaurant = image_path/f'{data_restaurant_selected['Name'][st.session_state.Restaurant_Recommendation[i]]}{ext}'
                if image_path_restaurant.exists():
                    image_path = image_path_restaurant
            st.image(str(image_path),use_column_width=True)
            with st.popover(data_restaurant_selected['Name'][st.session_state.Restaurant_Recommendation[i]]):
                place_recommended = folium.Map(location=[data_restaurant_selected['Latitude'][st.session_state.Restaurant_Recommendation[i]],data_restaurant_selected['Longitude'][st.session_state.Restaurant_Recommendation[i]]], zoom_start=50)
                folium.Marker(
                    [data_restaurant_selected['Latitude'][st.session_state.Restaurant_Recommendation[i]],data_restaurant_selected['Longitude'][st.session_state.Restaurant_Recommendation[i]]],
                    popup=data_restaurant_selected['Name'][st.session_state.Restaurant_Recommendation[i]],
                    tooltip=data_restaurant_selected['Name'][st.session_state.Restaurant_Recommendation[i]]
                ).add_to(place_recommended)

                folium_static(place_recommended,width=650,height=500)

                st.subheader('Description: ')
                st.subheader(f'{data_restaurant_selected['Description'][st.session_state.Restaurant_Recommendation[i]]}')

    
    


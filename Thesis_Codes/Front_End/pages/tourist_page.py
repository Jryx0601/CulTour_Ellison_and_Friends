import streamlit as st
import folium
from streamlit_folium import folium_static
import sys
from pathlib import Path
from PIL import Image

if 'Tourist_data' in st.session_state:
    if st.button('Back'):
        st.switch_page('pages/Home.py')

    st.header(st.session_state.Tourist_data['Name'])
    st.divider()

    place = folium.Map(location = [st.session_state.Tourist_data['Latitude'],st.session_state.Tourist_data['Longitude']], zoom_start=50)
    folium.Marker(
        [st.session_state.Tourist_data['Latitude'],st.session_state.Tourist_data['Longitude']],
        popup=st.session_state.Tourist_data['Name'],
        tooltip=st.session_state.Tourist_data['Name']
    ).add_to(place)

    folium_static(place, width = 1350, height= 725)
    st.divider()
    st.subheader(f'Description:')
    st.caption(f'{st.session_state.Tourist_data['Description']}')
    st.subheader('History:')
    st.caption(f'{st.session_state.Tourist_data['History']}')
    st.divider()

if 'Tourist_recommendation' in st.session_state:
    script_recommendation = Path(__file__).parent.parent.parent
    sys.path.append(str(script_recommendation))
    from Back_End.Recommender_Model import data_Attraction_selected

    script_location = Path(__file__).parent
    extensions = ['.jpg','.jfif','.png','.gif','.JPG','.jpeg']


    st.header(f'Similar You Might Like: ')
    col1,col2,col3,col4,col5 = st.columns(5)
    cols = [col1,col2,col3,col4,col5]

    for i in range(len(st.session_state.Tourist_recommendation)):
        with cols[i]:
            image_path = script_location/'Tourist_Attraction'
            for ext in extensions:
                image_path_tourist = image_path/f'{data_Attraction_selected['Name'][st.session_state.Tourist_recommendation[i]]}{ext}'
                if image_path_tourist.exists():
                    image_path = image_path_tourist
            image = Image.open(str(image_path))
            new_image = image.resize((450,400))
            st.image(new_image)
            with st.popover(data_Attraction_selected['Name'][st.session_state.Tourist_recommendation[i]],use_container_width=True):
                st.title(data_Attraction_selected['Name'][st.session_state.Tourist_recommendation[i]])
                place_recommended = folium.Map(location= [data_Attraction_selected['Latitude'][st.session_state.Tourist_recommendation[i]],data_Attraction_selected['Longitude'][st.session_state.Tourist_recommendation[i]]], zoom_start=50)
                folium.Marker(
                    [data_Attraction_selected['Latitude'][st.session_state.Tourist_recommendation[i]],data_Attraction_selected['Longitude'][st.session_state.Tourist_recommendation[i]]],
                    popup=data_Attraction_selected['Name'][st.session_state.Tourist_recommendation[i]],
                    tooltip=data_Attraction_selected['Name'][st.session_state.Tourist_recommendation[i]]
                ).add_to(place_recommended)

                folium_static(place_recommended,width=650,height=500)

                st.divider()
                st.subheader(f'Description:')
                st.caption(f'{data_Attraction_selected['Description'][st.session_state.Tourist_recommendation[i]]}')
                st.subheader(f'History:')
                st.caption(f'{data_Attraction_selected['History'][st.session_state.Tourist_recommendation[i]]}')

    
    


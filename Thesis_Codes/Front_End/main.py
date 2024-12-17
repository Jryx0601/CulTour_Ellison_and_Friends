import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
st.set_page_config(initial_sidebar_state="collapsed")
"""
To run this system make sure to locate the Front_End in the terminal then run: python -m streamlit run main.py
"""
with open('credential/account.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)


st.title("Log in to CulTour: ")
try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state['authentication_status']:
    st.session_state['authentication_status'] = True
    st.switch_page('pages/Home.py')
elif st.session_state['authentication_status'] is False:
    st.error('Username/Password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')


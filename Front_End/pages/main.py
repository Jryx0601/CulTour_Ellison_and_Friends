import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
st.set_page_config(initial_sidebar_state="collapsed")

with open('credential/account.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)



try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state['authentication_status']:
    authenticator.logout()
    st.switch_page('pages/Home.py')
elif st.session_state['authentication_status'] is False:
    st.error('Username/Password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
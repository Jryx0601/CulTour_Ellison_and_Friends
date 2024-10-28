import streamlit as st

st.title("Log In")
username = st.text_input("Username")

password = st.text_input("Password")
switch_page = st.button("Log in")
#Go to home page
if switch_page:
    st.switch_page("./Front_End/02_Home.py")

#Make an account
st.write("Don't have an account?")
sign_up_page = st.button("Sign Up")
if sign_up_page:
    st.switch_page("./Front_End/01.1_Sign-up.py")

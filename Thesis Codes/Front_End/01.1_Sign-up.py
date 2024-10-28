import streamlit as st

st.title("Sign up")

switch_page = st.button("Log in")

#Go to Log in page
if switch_page:
    st.switch_page("./Front_End/01_Log-in.py")
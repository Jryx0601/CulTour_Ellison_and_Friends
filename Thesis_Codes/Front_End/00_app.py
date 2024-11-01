#python -m streamlit run 00_app.py
import streamlit as st

st.set_page_config(
    page_title="Title ng page",
    page_icon='📃'
)
#TESTING
testbut = st.button("GO TESTING")
if testbut:
    st.switch_page("pages/01_Log-in.py")

st.sidebar.success("Select a page")

st.title("Testing app")
st.write("Hello world")
button1 = st.button("Click me")
#Activate the button
if button1:
    st.write("ola")

#Checkbox
like = st.checkbox("Do you like ellison?")

button2 = st.button("Submit")
if button2:
    if like:
        st.write("Hindi ka mahal ni ellison")
    else:
        st.write("Nice one")
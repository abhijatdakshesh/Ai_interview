import streamlit as st

st.title("Welcome to the AI-powered Interview Assistant by AIqwip")
st.write("This will help you submit your resume and prepare for your interview.")

if st.button("Start"):
    st.write("Please enter your Name:")
    name = st.text_input("Name:")
    st.write("Please enter your Email:")
    name = st.text_input("Email:")
    st.write("Please enter your Password:")
    name = st.text_input("Password:")
    st.button("Login")
else:
    st.write("Please click the button to start the interview.")



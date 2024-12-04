import sqlite3
import streamlit as st

# Initialize session state variables
if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "password" not in st.session_state:
    st.session_state.password = ""
if "resume" not in st.session_state:
    st.session_state.resume = None
if "step" not in st.session_state:
    st.session_state.step = 0

# Title
st.title("Wep")
st.write("This will help you submit your resume and prepare for your interview.")

with st.form(key='my_form'):
	text_input = st.text_input(label='Enter your name')
	text_email = st.text_input(label='Enter your Email')
	submit_button = st.form_submit_button(label='Submit')
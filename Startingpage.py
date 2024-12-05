import streamlit as st

# Initialize session state variables
if "name" not in st.session_state:
    st.session_state.name = "admin"
if "email" not in st.session_state:
    st.session_state.email = "abhijatdakshesh@com"
if "password" not in st.session_state:
    st.session_state.password = "admin"
if "resume" not in st.session_state:
    st.session_state.resume = None
if "step" not in st.session_state:
    st.session_state.step = 0

# Title
st.title("Welcome to AIqwip AI-powered Interview Assistant")
st.write("This will help you submit your resume and prepare for your interview.")

# Static credentials
static_name = "admin"
static_email = "abhijatdakshesh@com"
static_password = "admin"

# Display static credentials
st.write(f"**Name:** {static_name}")
st.write(f"**Email:** {static_email}")
st.write("**Password:** <hidden>")  # Do not display the password for security reasons

# Form for login validation
with st.form(key='my_form'):
    submit_button = st.form_submit_button(label='Login')

# Handle login button click
if submit_button:
    if (
        st.session_state.name == static_name and
        st.session_state.email == static_email and
        st.session_state.password == static_password
    ):
        st.success("Login successful!")
    else:
        st.error("Login failed. Static credentials are invalid.")

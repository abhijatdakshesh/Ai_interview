import streamlit as st

# Simulated user database (for real-world use, consider a database)
user_database = {
    "admin": "admin",
    "user1@example.com": "password123",
    "user2@example.com": "mypassword"
}

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login logic
if not st.session_state.logged_in:
    st.title("Login to AIqwip")
    with st.form(key="login_form"):
        email = st.text_input("Enter your Email")
        password = st.text_input("Enter your Password", type="password")
        login_button = st.form_submit_button("Login")
    
    if login_button:
        if email in user_database and user_database[email] == password:
            st.session_state.logged_in = True
            st.success(f"Welcome, {email}!")
        else:
            st.error("Invalid email or password. Please try again.")
else:
    st.title("AIqwip Dashboard")
    st.write("You are logged in!")
    logout_button = st.button("Logout")
    if logout_button:
        st.session_state.logged_in = False
        st.experimental_rerun()

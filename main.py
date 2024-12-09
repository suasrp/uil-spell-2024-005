import streamlit as st
import pickle
import datetime
import time
import streamlit_authenticator as stauth
import yaml

# Define timezone difference
DIFF_JST_FROM_UTC = 9
ent_time = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

start = time.time()

# Load configuration
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

# Create an authenticator instance
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'],
)

# User login process
name, authentication_status, username = authenticator.login('main', 'main')

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state["authentication_status"]:
    # Successful login
    authenticator.logout('Logout', 'main')
    st.write(f'Login successful')

    # Set session state flag for authentication
    st.session_state['authenticated'] = True

    # Redirect to the page after successful login
    st.experimental_rerun()  # Re-run to load the correct page (sp_ul_t06a_web.py)

elif st.session_state["authentication_status"] is False:
    st.error('The username or password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

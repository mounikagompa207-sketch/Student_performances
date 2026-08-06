import streamlit as st
import base64

from database import (
    create_users_table,
    create_students_table,
    login_user
)


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# Create Database Tables
# -----------------------------
create_users_table()
create_students_table()
# -----------------------------
# Background Image
# -----------------------------
def add_bg():
    with open("images/background.jpg", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .login-box {{
        background: rgba(255,255,255,0.12);
        padding:30px;
        border-radius:20px;
        backdrop-filter: blur(10px);
        box-shadow:0px 0px 20px rgba(0,0,0,.4);
    }}

    h1,h4,label,p {{
        color:white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

add_bg()

# -----------------------------
# Title
# -----------------------------
st.markdown("""
<h1 style='text-align:center'>
🎓 Student Performance Prediction System
</h1>

<h4 style='text-align:center'>
AI Powered Student Performance Analysis
</h4>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        user = login_user(username, password)

        if user:

            st.success(f"Welcome {user[1]}")

            st.session_state["logged_in"] = True

            st.session_state["username"] = username

            st.switch_page("pages/home.py")

        else:

            st.error("Invalid Username or Password")

    st.write("")

    if st.button("Create New Account", use_container_width=True):

        st.switch_page("pages/register.py")

    st.markdown("</div>", unsafe_allow_html=True)

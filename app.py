import streamlit as st

# -----------------------------
# LOGIN CREDENTIALS
# -----------------------------

USERNAME = "admin"
PASSWORD = "Project@123"

# -----------------------------
# SESSION STATE
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# LOGIN PAGE
# -----------------------------

def login():

    st.title("🔐 Login Page")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):

        if user == USERNAME and pwd == PASSWORD:

            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Wrong credentials")

# -----------------------------
# MAIN APP
# -----------------------------

def app():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go To",
        ["Home", "Project PPT", "Logout"]
    )

    # HOME PAGE
    if page == "Home":

        st.title("📊 Chocolate Sales Analysis")

        st.write("""
        Welcome to my Chocolate Sales Analysis Web App.

        Skills:
        - SQL
        - Python
        - Power BI
        - Excel
        - Streamlit
        """)

        st.success("Project Running Successfully")

    # PPT PAGE
    elif page == "Project PPT":

        st.header("📂 Project Presentation")

        st.write("Click below to download the project PPT.")

        with open("Chocolate Sales Analysis.pptx", "rb") as ppt:

            st.download_button(
                label="⬇ Download PPT",
                data=ppt,
                file_name="Chocolate_Sales_Analysis.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )

    
    # LOGOUT
    elif page == "Logout":

        st.session_state.logged_in = False
        st.rerun()

# -----------------------------
# APP START
# -----------------------------

if st.session_state.logged_in:
    app()
else:
    login()

    



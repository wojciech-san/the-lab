import streamlit as st
from streamlit_option_menu import option_menu

# Set page layout to wide for a better ribbon appearance
st.set_page_config(layout="wide")

# 1. Create the horizontal ribbon navigation
selected = option_menu(
    menu_title="Hi, there",  # Leave None to hide the title and keep it compact
    options=["Dashboard", "Analytics", "Settings"], 
    icons=["house", "bar-chart", "gear"], # Bootstrap icons
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "18px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# 2. Route the sections based on the selected tab
if selected == "Dashboard":
    st.title("Dashboard Section")
    st.write("Welcome to the main dashboard.")
    
elif selected == "Analytics":
    st.title("Analytics Section")
    st.write("Here are your hidden charts and data.")
    
elif selected == "Settings":
    st.title("Settings Section")
    st.write("Configure your app here.")
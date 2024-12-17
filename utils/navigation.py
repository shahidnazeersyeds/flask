import streamlit as st
from streamlit_option_menu import option_menu

def create_navigation():
    return option_menu(
        menu_title=None,
        options=["Home", "My Journey", "Projects", "Skills"],
        icons=["house", "clock-history", "laptop", "graph-up"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#3498db", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3498db"},
        },
    )
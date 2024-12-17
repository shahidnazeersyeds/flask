import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="DreamStream Portfolio",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS
    st.markdown("""
        <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .css-1d391kg {
            font-family: 'Open Sans', sans-serif;
        }
        body {
            font-family: 'Lato', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)
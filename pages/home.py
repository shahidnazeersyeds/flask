import streamlit as st
from utils.lottie_loader import load_lottie_url

def show_home_page():
    # Header Section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Welcome to DreamStream! 👋")
        st.subheader("Computer Science & Engineering Graduate")
        st.write("""
        I'm passionate about creating data-driven solutions and developing 
        innovative software applications. With expertise in Python, Data Science, 
        and Web Development, I transform complex problems into elegant solutions.
        """)
        
        # Quick Stats
        st.write("---")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Projects Completed", "3+")
        with col_b:
            st.metric("Certifications", "3")
        with col_c:
            st.metric("GPA", "8.8/10")
    
    with col2:
        # Add a professional animation
        lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        st.lottie(lottie_coding, height=300)
    
    # Featured Quote
    st.write("---")
    st.info(
        '"The only way to do great work is to love what you do." - Steve Jobs'
    )
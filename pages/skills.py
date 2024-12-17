import streamlit as st
import plotly.graph_objects as go
import numpy as np

def create_skills_radar():
    categories = [
        'Python', 'SQL', 'HTML/CSS',
        'Data Science', 'Web Development',
        'Visualization'
    ]
    
    values = [0.9, 0.8, 0.7, 0.85, 0.75, 0.8]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skills',
        line_color='#3498db'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=False
    )
    
    return fig

def show_skills_page():
    st.title("Skills & Expertise 🚀")
    
    # Technical Skills Section
    st.header("Technical Proficiency")
    
    # Radar Chart for Skills
    st.plotly_chart(create_skills_radar(), use_container_width=True)
    
    # Detailed Skills Breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Programming & Tools")
        skills_data = {
            "Python": 90,
            "SQL": 80,
            "HTML/CSS": 70,
            "Power BI": 85,
            "Excel": 80
        }
        
        for skill, proficiency in skills_data.items():
            st.write(f"{skill}")
            st.progress(proficiency/100)
    
    with col2:
        st.subheader("Soft Skills")
        soft_skills = [
            "Strong Communication",
            "Team Collaboration",
            "Leadership",
            "Critical Thinking",
            "Problem-Solving"
        ]
        
        for skill in soft_skills:
            st.write(f"✓ {skill}")
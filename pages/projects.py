import streamlit as st
import pandas as pd

def show_projects_page():
    st.title("Project Portfolio 💻")
    
    # Project Filter
    project_type = st.selectbox(
        "Filter by Category",
        ["All", "Data Science", "Web Development", "Business Analytics"]
    )
    
    # Project Cards
    projects = [
        {
            "title": "Rating Prediction of Google Play Store",
            "category": "Data Science",
            "description": "Predicted app ratings using data mining techniques with 85% accuracy",
            "tools": ["Python", "pandas", "scikit-learn"],
            "metrics": {"Accuracy": 85}
        },
        {
            "title": "Business Analytics Project",
            "category": "Business Analytics",
            "description": "Created interactive dashboards and automated reporting systems",
            "tools": ["Power BI", "MySQL", "Python"],
            "metrics": {"Efficiency Improvement": 20}
        },
        {
            "title": "Junior Software Developer Project",
            "category": "Web Development",
            "description": "Developed web-based automation tools",
            "tools": ["HTML", "CSS", "JavaScript", "MySQL"],
            "metrics": {"Task Completion Time Reduction": 40}
        }
    ]
    
    # Filter projects based on selection
    filtered_projects = projects if project_type == "All" else [p for p in projects if p["category"] == project_type]
    
    # Display projects in a grid
    cols = st.columns(3)
    for idx, project in enumerate(filtered_projects):
        with cols[idx % 3]:
            st.markdown(f"""
            <div style='padding: 1rem; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h3>{project['title']}</h3>
                <p><strong>Category:</strong> {project['category']}</p>
                <p>{project['description']}</p>
                <p><strong>Tools:</strong> {', '.join(project['tools'])}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display metrics
            for metric, value in project['metrics'].items():
                st.metric(metric, f"{value}%")
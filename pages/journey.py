import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

def create_timeline_data():
    return [
        {
            "title": "Bachelor of Technology",
            "description": "Computer Science & Engineering at AITS, Kadapa",
            "date": "2018 - 2022",
            "gpa": "8.8/10"
        },
        {
            "title": "Higher Secondary (12th)",
            "description": "Sri Chaitanya Junior College, Kadapa",
            "date": "2016 - 2018",
            "percentage": "74.8%"
        },
        {
            "title": "Secondary School (10th)",
            "description": "Nagarjuna Model School, Maruthinagar, Kadapa",
            "date": "2014 - 2016",
            "percentage": "67.98%"
        }
    ]

def show_journey_page():
    st.title("My Educational Journey 🎓")
    
    # Timeline visualization using Plotly
    timeline_data = create_timeline_data()
    
    fig = go.Figure(data=[
        go.Scatter(
            x=[item["date"].split(" - ")[0] for item in timeline_data],
            y=[1, 1, 1],
            mode="markers+text",
            text=[item["title"] for item in timeline_data],
            textposition="top center",
            marker=dict(size=20, color="#3498db"),
        )
    ])
    
    fig.update_layout(
        title="Educational Timeline",
        showlegend=False,
        height=400,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False, showticklabels=False),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed Education Information
    for item in timeline_data:
        with st.expander(f"{item['title']} ({item['date']})"):
            st.write(f"**Institution:** {item['description']}")
            if 'gpa' in item:
                st.write(f"**GPA:** {item['gpa']}")
            if 'percentage' in item:
                st.write(f"**Percentage:** {item['percentage']}")
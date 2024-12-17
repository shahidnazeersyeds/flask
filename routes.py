from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    technical_skills = {
        'Programming Languages': {
            'Python': 90,
            'SQL': 80,
            'HTML/CSS': 70
        },
        'Data Science Tools': {
            'Pandas': 85,
            'NumPy': 80,
            'Scikit-learn': 75,
            'TensorFlow': 70
        },
        'Web Frameworks': {
            'Flask': 85,
            'Django': 75,
            'Streamlit': 80
        }
    }
    
    soft_skills = [
        {'name': 'Strong Communication', 'icon': 'fas fa-comments'},
        {'name': 'Team Collaboration', 'icon': 'fas fa-users'},
        {'name': 'Leadership', 'icon': 'fas fa-crown'},
        {'name': 'Critical Thinking', 'icon': 'fas fa-brain'},
        {'name': 'Problem-Solving', 'icon': 'fas fa-puzzle-piece'}
    ]
    
    return render_template('skills.html', technical_skills=technical_skills, soft_skills=soft_skills)

@app.route('/journey')
def journey():
    milestones = [
        {
            'date': '2018 - 2022',
            'title': 'Bachelor of Technology – Computer Science & Engineering',
            'description': 'Annamacharya Institute of Technology and Sciences, Kadapa',
            'gpa': '8.8/10'
        },
        {
            'date': '2016 - 2018',
            'title': 'Higher Secondary (12th) – PCM',
            'description': 'Sri Chaitanya Junior College, Kadapa',
            'percentage': '74.8%'
        },
        {
            'date': '2014 - 2016',
            'title': 'Secondary School (10th)',
            'description': 'Nagarjuna Model School, Maruthinagar, Kadapa',
            'percentage': '67.98%'
        }
    ]
    return render_template('journey.html', milestones=milestones)
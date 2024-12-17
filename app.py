from flask import Flask, render_template
from flask_assets import Environment, Bundle
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Assets
assets = Environment(app)

# Bundle and minify CSS files
css = Bundle(
    'scss/main.scss',
    filters='libsass,cssmin',
    output='css/main.min.css'
)
assets.register('css', css)

# Bundle and minify JavaScript files
js = Bundle(
    'js/animations.js',
    'js/parallax.js',
    'js/projects.js',
    filters='jsmin',
    output='js/main.min.js'
)
assets.register('js', js)

# Import routes after app initialization to avoid circular imports
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
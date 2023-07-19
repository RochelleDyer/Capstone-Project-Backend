from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('http://localhost:5173/')

@site.route('/profile')
def profile():
    return render_template('profile.html')



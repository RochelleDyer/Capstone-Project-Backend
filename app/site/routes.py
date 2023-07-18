from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/genres')
def genres():
    return render_template('genres.html')

@site.route('/favs')
def favs():
    return render_template('spotify.html')

@site.route('/contact')
def contact():
    return render_template('contact.html')

@site.route('/spotify')
def spotify():
    return render_template ('favs.html')


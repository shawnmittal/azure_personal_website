from flask import Blueprint, render_template, url_for

mod = Blueprint('website', __name__, 
                template_folder='templates', 
                static_folder='static',
                static_url_path='/website/static')  

@mod.route('/')
def home():
    return render_template('website/home.html')

@mod.route('/timeline')
def timeline():
    return render_template('website/timeline.html')

@mod.route('/projects')
def projects():
    return render_template('website/projects.html')

@mod.errorhandler(404)
def page_not_found(e):
    return render_template('website/404.html'), 404

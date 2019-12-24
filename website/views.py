from flask import Flask, render_template
from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

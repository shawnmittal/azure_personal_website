from flask import Flask

app = Flask(__name__)

from web_app.website.views import mod
from web_app.bokeh_example.views import dashboard
from web_app.nlp_example.views import nlpExample

app.register_blueprint(mod)
app.register_blueprint(dashboard, url_prefix='/projects')
app.register_blueprint(nlpExample, url_prefix='/projects')
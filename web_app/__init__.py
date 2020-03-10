from flask import Flask

app = Flask(__name__)

from web_app.website.views import mod
from web_app.bokeh_example.views import dashboard

app.register_blueprint(mod)
app.register_blueprint(dashboard, url_prefix='/projects')
from flask import Blueprint

mod = Blueprint('bokeh_example', __name__)

@mod.route('/bokeh_example')
def bokeh_example():
    return '<h1>Bokeh Example</h1>'
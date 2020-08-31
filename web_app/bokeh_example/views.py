from flask import Blueprint, render_template, request
from .charting.helper import redraw, components

dashboard = Blueprint(
    "bokeh_example",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/bokeh_example/static",
)


@dashboard.route("/bokeh_example", methods=["GET", "POST"])
def bokeh_example():
    selected_class = request.form.get("dropdown-select")

    if selected_class == 0 or selected_class == None:
        survived_chart, title_chart, hist_age = redraw(1)
    else:
        survived_chart, title_chart, hist_age = redraw(selected_class)

    script_survived_chart, div_survived_chart = components(survived_chart)
    script_title_chart, div_title_chart = components(title_chart)
    script_hist_age, div_hist_age = components(hist_age)

    return render_template(
        "bokeh_example/dashboard.html",
        div_survived_chart=div_survived_chart,
        script_survived_chart=script_survived_chart,
        div_title_chart=div_title_chart,
        script_title_chart=script_title_chart,
        div_hist_age=div_hist_age,
        script_hist_age=script_hist_age,
        selected_class=selected_class,
    )

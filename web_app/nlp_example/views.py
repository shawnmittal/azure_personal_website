import requests
from flask import Blueprint, redirect, request, url_for, jsonify, render_template

# NLP packages
from .parse_and_eval import get_and_parse, vader

nlpExample = Blueprint('nlp_example', __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/nlp_example/static')


@nlpExample.route('/nlp_example/api', methods=['POST'])
def eval_url():
    url = request.get_json()
    article = get_and_parse(url)
    sentiment = vader(article)
    return jsonify(
        title=article.title,
        summary=article.summary,
        keywords=article.keywords,
        score=sentiment)

@nlpExample.route('/nlp_example/frontend', methods=['POST', 'GET'])
def nlp_frontend():
    if request.method == 'POST':
        selected_url = request.form.get('url-select')
        article = get_and_parse(selected_url)
        sentiment = vader(article)
    else:
        selected_url = 'https://www.cnn.com/2020/08/17/us/coronavirus-college-university/index.html'
        article = get_and_parse(selected_url)
        sentiment = vader(article)

    return render_template(
        'nlp_example/frontend.html',
        selected_url = article.source_url,
        article_title = article.title,
        article_keywords = article.keywords,
        article_summary = article.summary,
        article_sentiment = sentiment
    )
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
import datetime
from flask import Blueprint, render_template

from article.models import Article

article_bp = Blueprint('article', __name__, url_prefix='/article')
article_bp.template_folder = './templates'

@article_bp.route('/index')
def idnex():
    articles = Article.query.order_by(Article.created.desc()).all()
    return render_template('index.html',articles=articles)
import datetime

from flask import Blueprint, render_template, request, redirect

from article.models import Article
from libs.orm import db

article_bp = Blueprint('article', __name__, url_prefix='/article')
article_bp.template_folder = './templates'


@article_bp.route('/index')
def idnex():
    articles = Article.query.order_by(Article.created.desc()).all()
    return render_template('index.html', articles=articles)


@article_bp.route('/post', methods=('post', 'get'))
def post_article():
    if request.method == 'post':
        title = request.form.get('title')
        content = request.form.get('content')
        now = datetime.datetime.now()

        article = Article(title=title, content=content, created=now)
        db.session.add(article)
        db.session.commit()
        return render_template('/article/read?aid=%s' % article.id)
    else:
        return render_template('post.html')


@article_bp.route('/read')
def read_article():
    aid = int(request.args.get('aid'))
    article = Article.query.get(aid)
    return render_template('read.html', article=article)


@article_bp.route('/delete')
def delete_article():
    aid = int(request.args.get('aid'))
    Article.query.fileter_by(id=aid).delete()
    db.session.commit()
    return redirect('/article/index')
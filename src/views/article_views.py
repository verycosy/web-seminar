from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

bp = Blueprint('article', __name__, url_prefix='/article')

articles = []

@bp.route('/')
def article_list():
    return render_template('article/list.html', articles=articles)

@bp.route('/new', methods=['POST', 'GET'])
def new_article():
    if request.method == 'GET':
        return render_template('article/new.html')
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        article = {
            "id": len(articles),
            "title": title,
            "content": content
        }

        articles.append(article)
        return redirect(url_for('article.detail', article_id=article['id']))
        

@bp.route('/<int:article_id>', methods=['GET', 'DELETE'])
def detail(article_id):
    if request.method == 'GET':
        article = articles[article_id]
        return render_template('article/detail.html', article=article)
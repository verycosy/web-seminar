from flask import Flask, jsonify, render_template
from views import article_views

app = Flask(__name__)
app.config['SECRET_KEY'] = "JNU"
app.register_blueprint(article_views.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1")
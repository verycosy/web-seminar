from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About'


@app.route('/data')
def data():
    data = {
        "name": "이승기",
        "age": 33
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host="127.0.0.1")
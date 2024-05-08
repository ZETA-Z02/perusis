from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chatbot')
def chat():
    return render_template('chatbot.html')


if __name__ == '__main__':
    app.run(debug=True)

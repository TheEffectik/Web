from flask import render_template
from flask import Flask, redirect
import random
import json
from wtforms.validators import DataRequired
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

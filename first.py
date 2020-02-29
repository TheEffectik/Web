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


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=random.randint(1, 10**3))

@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/ochered')
def o():
    return render_template('ochered.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


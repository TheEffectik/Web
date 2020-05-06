from flask import render_template, request, url_for
from flask import Flask, redirect
import random
import json
from wtforms.validators import DataRequired
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

item = ['/astronaut_selection', '/choice/<planet_name>', '/results/<nickname>/<int:level>/<float:rating>']

@app.route('/')
def index():
    global item
    return render_template('base.html', item=item)




@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center" >Анкета претендента</h1>
                            <p align="center" > на участие в миссии</p>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="password" class="form-control" id="name" placeholder="Введите имя" name="name">

                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label></div>

<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Пилот</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Строитель</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Экзобиолог</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Врач</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Инженер по терраформированию</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Климатолог</label></div>
<div class="form-group form-check"><input type="checkbox" class="form-check-input" id="acceptRules" name="accept"><label class="form-check-label" for="acceptRules">Специалист по радиационной защите</label></div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-group">
                                        <label for="about">Почему вы хотите оказаться на марсе?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                        <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return render_template('rating.html', nickname=nickname, level=level, rating=rating)

@app.route('/choice/<planet_name>')
def planet(planet_name):
    return render_template('mars.html', planet=planet_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

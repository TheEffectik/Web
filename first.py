from flask import render_template, request, url_for
from flask import Flask, redirect
import random
import json
from wtforms.validators import DataRequired
from loginform import LoginForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

item = ['/astronaut_selection', '/choice/<planet_name>', '/results/<nickname>/<int:level>/<float:rating>', '/carousel',
        '----------flask.wtf---------',
        '/training/<prof> - Тренировки в полете, flask.wtf', '/list_prof - Список професий', '/answer или /auto_answer'
                                                                                             '- Автоматический ответ',
        '/login - Двойная защита', '/distribution - по каютам', '/table/<sex>/<int:age> - ну собсна таблица']
list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию']
cabin = ['Риддли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
images = ['https://images.wallpaperscraft.ru/image/pustynya_gory_pesok_nebo_pejzazh_100762_1152x864.jpg',
          'https://avatars.mds.yandex.net/get-zen_doc/60857/pub_5c0a324c59f30300aa95a927_5c130f9232fd3100a9752c2b/scale_1200',
          'https://cdn.photosight.ru/img/7/487/6505893_xlarge.jpg']
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    img = ''
    color = '#'
    if age <= 21:
        img = '/static/img/mini.png'
    else:
        img = '/static/img/big.png'
    colors_f = ['ef0097', 'fe28a2', 'ff1493', 'ff43a4', 'f664af', 'dd4492', 'cd2682', 'cd2682', 'ca2c92', 'bd33a4',
              '991199']
    colors_m = ['0000ff', '00008b', '082567', '1e2460', '1a153f', '240935', '20155e', '191970', '310062', '32127a',
                '4b0082']
    if sex == 'male':
        if age < 100:
            color += colors_m[age % 10]
        else:
            color += colors_m[-1]
    else:
        if age < 100:
            color += colors_f[age % 10]
        else:
            color += colors_f[-1]
    return render_template('table.html', img=img, color=color)


@app.route('/distribution')
def distribution():
    global cabin
    return render_template('distribution.html', list=cabin, len=len(cabin))

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/')
def index():
    global item
    return render_template('base.html', item=item)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    dict ={'title': 'татйтле', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего', 'profession': 'штурман',
           'sex': 'male', 'motivation': 'Всегда мечтал застрять на марсе!', 'ready': True}
    return render_template('auto_answer.html', dict=dict)


@app.route('/list_prof')
def list_prof():
    list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию']
    return render_template('list_prof.html', list_prof=list_prof)


@app.route('/training/<prof>')
def prof(prof):
    return render_template('prof.html', prof=prof, title=prof)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/carousel', methods=['POST', 'GET'])
def car():
    global images
    if request.method == 'GET':
        return render_template('carousel.html', images=images, len=len(images))
    elif request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(len(images) + 1) + filename[-4:]))
        images.append('/static/img/' + str(len(images) + 1) + str(filename[-4:]))
        return render_template('carousel.html', images=images, len=len(images))



@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return render_template('rating.html', nickname=nickname, level=level, rating=rating)


@app.route('/choice/<planet_name>')
def planet(planet_name):
    return render_template('mars.html', planet=planet_name)


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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

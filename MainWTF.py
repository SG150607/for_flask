from flask import Flask
from flask import url_for
from flask import render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/odd_event')
def odd_even():
    return render_template('odd_event.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/line')
def line():
    return render_template('line.html')


@app.route('/list_prof/<mod>')
def list_print(mod):
    with open('list_prof', 'r', encoding="utf8") as data:
        listt = data.read()
    return render_template('list_print.html', listt=listt, mod=mod)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

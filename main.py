from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def shoutout():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.',
                         'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.',
                         'И начнем с Марса!', 'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}"
                     "alt="здесь должна была быть картинка, но не нашлась"> 
                    <t></br>Вот она какая, красная планета.</t>
                  </body> 
                </html> """


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                     <h1>Жди нас, Марс!</h1>
                     <img src="{url_for('static', filename='img/mars.jpg')}"
                     "alt="здесь должна была быть картинка, но не нашлась">
                     <div class="one">Человечество вырастает из детства</div>
                     <div class="two">Человечеству мала одна планета</div>
                     <div class="three">Мы сделаем обитаемыми безжизненные пока планеты</div>
                     <div class="four">И начнем с Марса!</div>
                     <div class="five">Присоединяйся!</div>
                  </body> 
                </html> """


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите вашу фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите ваше имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Дошкольное</option>
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group>
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="research engineer" value="research engineer">
                                          <label class="form-check-label" for="research engineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="navigator" value="navigator">
                                          <label class="form-check-label" for="navigator">
                                            Штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="builder" value="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="cyber engineer" value="cyber engineer">
                                          <label class="form-check-label" for="cyber engineer">
                                            Киберинженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="exobiologist" value="exobiologist">
                                          <label class="form-check-label" for="exobiologist">
                                            Экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="astrogeologist" value="astrogeologist">
                                          <label class="form-check-label" for="astrogeologist">
                                            Астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="work" id="meteorologist" value="meteorologist">
                                          <label class="form-check-label" for="meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                    </div> 
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
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['work'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form.get('accept'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planets_info(planet_name):
    if planet_name == "Меркурий":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Наименьшая планета Солнечной системы</div>
                        <div class="alert alert-secondary">Самая близкая к Солнцу</div>
                        <div class="alert alert-info">Движется по небу быстрее других планет</div>
                        <div class="alert alert-info">можно увидеть только в течение небольшого времени после захода или до восхода солнца, обычно в сумерках</div>
                      </body>
                    </html>'''
    elif planet_name == "Венера":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Шестая по размеру планета Солнечной системы</div>
                        <div class="alert alert-secondary">Вторая по удалённости от Солнца</div>
                        <div class="alert alert-info">Имеет самый длинный период вращения вокруг своей оси среди всех планет</div>
                        <div class="alert alert-info">Венера не имеет естественных спутников</div>
                      </body>
                    </html>'''
    elif planet_name == "Земля":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Пятая по диаметру и массе среди всех планет Солнечной системы</div>
                        <div class="alert alert-secondary">Третья по удалённости от Солнца</div>
                        <div class="alert alert-info">Крупнейшая среди планет земной группы</div>
                        <div class="alert alert-info">Единственное известное человеку в настоящее время тело во Вселенной, населённое живыми организмами</div>
                      </body>
                    </html>'''
    elif planet_name == "Марс":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Седьмая по размеру планета Солнечной системы</div>
                        <div class="alert alert-secondary">Четвёртая по удалённости от Солнца</div>
                        <div class="alert alert-info">Марс называют «красной планетой» из-за красноватого оттенка поверхности, придаваемого ей минералом маггемитом</div>
                        <div class="alert alert-info">У Марса есть два естественных спутника — Фобос и Деймос</div>
                      </body>
                    </html>'''
    elif planet_name == "Юпитер":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Крупнейшая планета Солнечной системы</div>
                        <div class="alert alert-secondary">Пятая по удалённости от Солнца</div>
                        <div class="alert alert-info">Исследования Юпитера проводятся при помощи наземных и орбитальных телескопов</div>
                        <div class="alert alert-info">Юпитер имеет,по крайней мере, 92 спутника</div>
                      </body>
                    </html>'''
    elif planet_name == "Сатурн":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Вторая по размерам планета в Солнечной системе</div>
                        <div class="alert alert-secondary">Шестая планета по удалённости от Солнца</div>
                        <div class="alert alert-info">Сатурн обладает заметной системой колец, состоящей главным образом из частичек льда, меньшего количества тяжёлых элементов и пыли</div>
                        <div class="alert alert-info">На орбите Сатурна находилась автоматическая межпланетная станция (АМС) «Кассини»</div>
                      </body>
                    </html>'''
    elif planet_name == "Уран":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">Третья по диаметру и четвёртая по массе планета в Солнечной системе</div>
                        <div class="alert alert-secondary">Седьмая по удалённости от Солнца</div>
                        <div class="alert alert-info">Уран стал первой планетой, обнаруженной в Новое время и при помощи телескопа</div>
                        <div class="alert alert-info">У Урана имеется система колец и магнитосфера,а кроме того, 27 спутников</div>
                      </body>
                    </html>'''
    elif planet_name == "Нептун":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">По массе является третьей среди планет Солнечной системы, а по экваториальному диаметру Нептун занимает четвёртое место</div>
                        <div class="alert alert-secondary">Восьмая и самая дальняя от Солнца</div>
                        <div class="alert alert-info">Планета названа в честь Нептуна — римского бога морей</div>
                        <div class="alert alert-info">В атмосфере Нептуна бушуют самые сильные ветры среди планет Солнечной системы</div>
                      </body>
                    </html>'''
    elif planet_name == "Плутон":
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>{planet_name}</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert alert-primary">По массе является третьей среди планет Солнечной системы, а по экваториальному диаметру Нептун занимает четвёртое место</div>
                        <div class="alert alert-secondary">Восьмая и самая дальняя от Солнца</div>
                        <div class="alert alert-info">Планета названа в честь Нептуна — римского бога морей</div>
                        <div class="alert alert-info">В атмосфере Нептуна бушуют самые сильные ветры среди планет Солнечной системы</div>
                      </body>
                    </html>'''
    else:
        return f'''<!doctype html>
                   <html lang="en">
                     <head>
                       <meta charset="utf-8">
                       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                      <link rel="stylesheet"
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                      crossorigin="anonymous">
                       <title>{planet_name}</title>
                     </head>
                     <body>
                       <h1>Не знаю такой планеты ¯\_(ツ)_/¯</h1>
                     </body>
                   </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def form_results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>{nickname}</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                    <div>составляет {rating}!</div>
                    <div class="alert alert-warning">Желаем удачи!</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

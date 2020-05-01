from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from app.forms import EditProfileForm
from app.forms import PostForm
from app.models import Post


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required      #декоратор login_required  защищает функцию просмотра от анонимных пользователей
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)                   #Добавление новой записи
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    posts = current_user.followed_posts()
    return render_template("index.html", title='Форум', form=form, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()    #filter_by() — запрос, вкл объекты, у которых совпадает имя
        if user is None or not user.check_password(form.password.data):     #check_password() - проверка пароля
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)                    #login_user() - регистрация пользователя при входе
        return redirect(url_for('main'))
    return render_template('login.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Обработка регистрации пользователя
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, breed=form.breed.data, petname=form.petname.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('register.html', title='Регистрация', form=form)

# Страница профиля пользователя
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()   #Загрузка пользователя из базы данных, используя запрос по имени пользователя.
                                                                    #first_or_404() в случае отсутствия результатов автоматически обратно клиенту отправляется ошибка 404.

    return render_template('user.html', title='Профиль', user=user)

# Редактор профиля
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data      #Копируем данные из формы
        current_user.breed = form.breed.data
        current_user.petname = form.petname.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('main'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.breed.data = current_user.breed
        form.petname.data = current_user.petname
        form.email.data = current_user.email
    return render_template('edit_profile.html', title='Редактор профиля', form=form)


# Главная страница
@app.route('/main')
@login_required
def main():
    return render_template('main.html', title='Главная страница')


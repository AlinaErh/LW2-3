from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    breed = StringField('Порода питомца', validators=[DataRequired()])
    petname = StringField('Кличка питомца', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Готово')

    def validate_username(self, username):                              # Проверка на наличие имени пользователя в БД
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Такое имя уже существует.')

    def validate_email(self, email):                                    # Проверка на наличие почты в БД
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Такой Email уже существует.')

# Редактор профиля
class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    breed = StringField('Порода питомца', validators=[DataRequired()])
    petname = StringField('Кличка питомца', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Сохранить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):                                      # Проверка дублирования имени
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Такое имя уже существует.')

#Форма для ввода сообщения
class PostForm(FlaskForm):
    post = TextAreaField('Оставить запись', validators=[DataRequired(), Length(min=1, max=3000)])
    submit = SubmitField('Отправить')
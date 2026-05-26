from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')

class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[
        DataRequired(),
        Length(min=3, max=64, message='Kullanıcı adı 3-64 karakter olmalı')
    ])
    email = StringField('E-posta Adresi', validators=[
        DataRequired(),
        Email(message='Geçerli bir email adresi girin')
    ])
    password = PasswordField('Şifre', validators=[
        DataRequired(),
        Length(min=6, message='Şifre en az 6 karakter olmalı')
    ])
    password2 = PasswordField('Şifreyi Onayla', validators=[
        DataRequired(),
        EqualTo('password', message='Şifreler eşleşmiyor')
    ])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, username):
        from app import db
        user = db.session.execute(db.select(User).filter_by(username=username.data)).scalar()
        if user:
            raise ValidationError('Bu kullanıcı adı zaten alınmış.')

    def validate_email(self, email):
        from app import db
        user = db.session.execute(db.select(User).filter_by(email=email.data)).scalar()
        if user:
            raise ValidationError('Bu email adresi zaten kayıtlı.')

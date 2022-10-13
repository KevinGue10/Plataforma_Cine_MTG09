from flask_wtf import FlaskForm
from wtforms import  Form,StringField, PasswordField, BooleanField, submitField
from wtforms.validators import DataRequired
class FormInicio(FlaskForm):
    usuario=StringField('nombre', validators=[DataRequired(message='No dejar vacio, completar')])
    contraseña=PasswordField('contraseña', validators=[DataRequired(message='No dejar vacio, completar')])
    recordar=BooleanField('Recordar Usuario')
    enviar=submitField('Iniciar Sesion')
    
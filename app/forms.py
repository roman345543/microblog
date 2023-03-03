from flack_wtf import FlaskForm
from wtfroms import StringField, PasswordField, SubmitField, BooleanField
from wtfroms.validators import  DataRequired

class LoginFrom(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    subnit = SubmitField('Sign In')


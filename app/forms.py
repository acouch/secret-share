from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ShareForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    confidante = StringField('confidante', validators=[DataRequired()])
    secret = StringField('secret', validators=[DataRequired()])
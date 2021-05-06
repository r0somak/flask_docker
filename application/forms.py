from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SaveDataForm(FlaskForm):
    name = StringField('Name')
    surname = StringField('Surname')
    submit = SubmitField('Save')
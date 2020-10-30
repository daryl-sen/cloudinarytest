from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

class upload_form(FlaskForm):
    file = FileField('Upload Image')
    submit = SubmitField()
from flask_wtf import Form
from wtforms import SubmitField,validators,TextField,TextAreaField
from wtforms.fields.html5 import EmailField

class formone(Form):
    name=TextField('Name :  ',validators=[validators.DataRequired()])
    usn=TextField('Usn : ',validators=[validators.DataRequired(),validators.Length(min=10,max=11)])
    email=EmailField('Email : ',validators=[validators.DataRequired(),validators.Email()])
    articledata=TextAreaField('Article : ',validators=[validators.DataRequired(),validators.Length(min=10)])
    
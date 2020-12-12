from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class FillInForm(FlaskForm):
    position = StringField(validators=[DataRequired()])
    location = StringField(validators=[DataRequired()])
    submit = SubmitField("Apply")

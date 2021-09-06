from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import required


class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators=[required()])
    review = TextAreaField('Movie review', validators=[required()])
    submit = SubmitField('Submit review')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content1 = TextAreaField('Content - සිංහල', validators=[DataRequired()])
    content2 = TextAreaField('Content - English', validators=[DataRequired()])
    submit = SubmitField('Post')

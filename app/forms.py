from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, NumberRange, Optional

from app.models import User

class RecipeForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(max=150)]
    )
    description = TextAreaField(
        "Description",
        validators=[DataRequired()]
    )
    instructions = TextAreaField(
        "Instructions",
        validators=[DataRequired()]
    )
    prep_time = IntegerField(
        "Prep Time",
        validators=[DataRequired(), NumberRange(min=1)]
    )
    submit = SubmitField()

class FeedbackForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField(
        "Email",
        validators = [DataRequired(), Email(), Length(max=120)])
    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10, max=500)])
    topic = StringField(
        "Topic",
        validators=[DataRequired(), Length(max=100)])

    submit = SubmitField("Send Feedback")

class ProfileForm(FlaskForm):
    display_name = StringField("Display Name", validators=[DataRequired(), Length(min=2, max=80)])
    bio = TextAreaField("Bio", validators=[Optional(), Length(max=80)])
    favorite_cuisine = StringField("Favorite Cuisine")
    years_cooking = IntegerField("Years Cooking", validators=[Optional(), NumberRange(min=0, max=100)])
    submit = SubmitField("Save Profile")
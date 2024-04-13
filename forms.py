from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    name = StringField('Pet name', validators=[InputRequired()],)
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("bunny", "Bunny")],)
    photo_url = StringField('Photo URL', validators=[Optional(), URL()],)
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=100)], )
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)],)


class EditPetForm(FlaskForm):
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
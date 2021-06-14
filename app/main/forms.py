from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, FileField
from wtforms.validators import Required

class AddPitch(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = TextAreaField("Description", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("Interview", "Interview"),("funny","Funny"),("Promotion","Promotion"),("Product","Product"),("Random","Random")],validators = [Required()]
    )
    submit = SubmitField("Add pitch")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')
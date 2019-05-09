from flask_wtf import FlaskForm
from wtforms import BooleanField ,StringField, validators,DateTimeField,TextAreaField,\
    IntegerField,SubmitField

class RegisterationForm(FlaskForm):
    username = StringField( "username", [validators.length(min=4,max=25)])
    email = StringField( 'Email Address', [validators.length(min=6,max=35)])
    accept_rules = BooleanField('I accecpt the site ruls', [validators.InputRequired()])
    submit = SubmitField(label="submit")

class ProfileForm(FlaskForm):
    birthday  = DateTimeField( label='Your Birthday', format='%m/%d/%y')
    signature = TextAreaField(label='Forum Signature')

class AdminProfileForm(ProfileForm):
    username = StringField(label='Username', validators=[validators.Length(max=40)])
    level    = IntegerField(label='User Level', validators=[validators.NumberRange(min=0, max=10)])


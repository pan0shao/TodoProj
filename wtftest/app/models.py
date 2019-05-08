from wtforms import Form,BooleanField , StringField, validators

class RegisterationForm(Form):
    username = StringField('username', [validators.length(min=4,max=25)])
    email = StringField('Email Address', [validators.length(min=6,max=35)])
    accept_rules = BooleanField('I accecpt the site ruls',
                                [validators.InputRequired()])





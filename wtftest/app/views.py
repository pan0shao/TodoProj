from app import app
from flask import render_template, request
from app.models import RegisterationForm,ProfileForm



@app.route('/')
def index():
    return render_template( "index.html" , site_name="ceshi")

@app.route('/wtf')
def tform():
    forms = RegisterationForm()
    if forms.validate_on_submit():
        messege="success !!"
    return render_template( "index.html" , form=forms, message=messege )


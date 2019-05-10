from app import app
from flask import render_template, request
from app.models import RegisterationForm,ProfileForm



@app.route('/')
def index():
    return render_template( "index.html" , site_name="ceshi")

@app.route('/wtf',methods=['POST','GET'] )
def tform():
    tforms = RegisterationForm( request.form ):
    message = ''
    if request.method == 'POST':
        tforms.username
        message = "success !!"
    return render_template( "index.html" , forms=tforms, messages=message )


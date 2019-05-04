from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@192.168.1.135:3306/todo'
#加载配置
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views,models






#配置flask-sqlalchemy
SECRET_KEY = 'todo'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.1.34:3306/todo'
SQLALCHEMY_TRACK_MODIFICATIONS = True

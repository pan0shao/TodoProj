from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#新建表
sql = "create table student( \
id int not null primary key, \
name varchar(50), \
age int, \
address varchar(100)\
);"

engine = create_engine('mysql+pymysql://root:123456@192.168.3.76/tests')

#表示获取到数据库连接。类似我们在MySQLdb中游标course的作用。
conn = engine.connect()

conn.execute(sql)



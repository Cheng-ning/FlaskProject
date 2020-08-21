from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    gender = db.Column(db.Enum('男', '女', '保密'))
    city = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.Date, default='1990-01-01')
    bio = db.Column(db.Text)
    money = db.Column(db.Float)





@app.route('/')
def home():
    users = Student.query.all()
    return render_template('home.html',users=users)

@manager.command
def add_table():
    '''添加表结构'''
    db.create_all()

@manager.command
def add_data():
    '''添加初始数据'''
    u1 = Student(name='tom', gender='男', city='北京', birthday='1990-2-3', bio='哈哈', money=12)
    u3 = Student(name='lucy', gender='女', city='上海', birthday='1995-12-23', bio='嘻嘻', money=32)
    u5 = Student(name='jack', gender='男', city='武汉', birthday='1998-1-2', bio='班长', money=34)
    u4 = Student(name='bob', gender='男', city='苏州', birthday='1978-3-5', bio='啦啦', money=4543)
    u6 = Student(name='lily', gender='女', city='南京', birthday='1989-3-5', bio='路路', money=65)
    u7 = Student(name='eva', gender='女', city='芜湖', birthday='1998-2-23', bio='马路', money=67)
    u8 = Student(name='alex', gender='男', city='成都', birthday='1996-3-4', bio='路仔', money=77)
    u9 = Student(name='jam', gender='男', city='太原', birthday='1993-2-9', bio='红路', money=98)
    u2 = Student(name='rob', gender='男', city='青岛', birthday='1992-2-1', bio='马露露', money=564)
    u10 = Student(name='ella', gender='女', city='大连', birthday='1990-12-30', bio='马仔', money=2223)

    db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10])
    db.session.commit()

if __name__ == '__main__':
    manager.run()
    # 创建表结构
    # db.create_all()

    # 插入多条数据
    # db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9, u10])
    # db.session.commit()

    # u10 = Student.query.get(10)
    # db.session.delete(u10)
    # db.session.commit()

    # Student.query.filter_by(gender='男').all()
    # Student.query.filter_by(id=3).one()
    #
    # for u in Student.query.filter_by(gender='男').order_by(Student.birthday.desc()):
    #     print(u.id, u.birthday, u.name)
    #
    # for u in Student.query.filter_by(gender='男').order_by(Student.birthday.desc()).limit(3):
    #     print(u.id, u.birthday, u.name)
    #
    # for u in Student.query.filter_by(gender='男').order_by(Student.birthday.desc()).limit(2).offset(3):
    #     print(u.id, u.birthday, u.name)
    #
    # Student.query.filter_by(gender='男').count()

    # 判断是否存在
    # result = Student.query.filter_by(gender='女').exists()
    # print(db.session.query(result).scalar())
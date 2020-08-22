#!/usr/bin/env python
# coding = UTF-8

from flask import Flask
from flask import redirect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp
from article.views import article_bp

app = Flask(__name__)
app.secret_key = r'(*&^TRF@QSR^&*Ijhu*()OKJU*(87ytGHU7654rE43Wr5$#Er56&*())(*Ikl;[}+_)'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


app.register_blueprint(user_bp)
app.register_blueprint(article_bp)


@app.route('/')
def home():
    return redirect('/article/index')


if __name__ == "__main__":
    manager.run()

from flask import Blueprint, request, render_template, session, redirect
from libs.orm import db
from user.models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'

@user_bp.route('/register', methods=('post', 'get'))
def register():
    if request.method == 'post':
        username = request.form.get('username')
        password = request.form.get('password')
        city = request.form.get('city')

        user = User(username=username, password=password, city=city)
        db.session.add(user)
        db.session.commit()
        return redirect('/user/login')
    else:
        return render_template('register.html')
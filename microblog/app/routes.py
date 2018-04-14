from app import app
<<<<<<< HEAD
from flask import render_template
=======
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
>>>>>>> ca3e4ef8e7b6cc8ba5ee6484b624802d643da675

@app.route('/')
@app.route('/index')
def index():
<<<<<<< HEAD
    user = {'username': 'GWesley'}
=======
    user = {'username' : 'GWesley'}
>>>>>>> ca3e4ef8e7b6cc8ba5ee6484b624802d643da675
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
<<<<<<< HEAD
    return render_template('index.html',title='Home',user=user, posts=posts)
=======
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if  current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
>>>>>>> ca3e4ef8e7b6cc8ba5ee6484b624802d643da675

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from datetime import date


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Katie Ford'}
    today = date.today().strftime("%d/%m/%y")
    exercise = {'exercise': '5 x 5 reps - Squats'}
    book = {'author': 'Yvon Chouinard', 'title': 'Let My People Go Surfing'}
    playlist = {'title': "Wilson's Morning Wake Up", 'url': 'http://spotify.com'}
   
    return render_template(
        'index.html', 
        title='Home', 
        user=user,
        today=today, 
        exercise=exercise,
        book=book,
        playlist=playlist
        )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


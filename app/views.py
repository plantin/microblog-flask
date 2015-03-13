__author__ = 'Tarly'
from app import app
from flask import render_template,flash,redirect
from forms import LoginForm
@app.route('/')
def show():
    user = {'nickname': 'Muel'} # fake user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Nanjing'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'I love Beijing!'
        }
    ]
    return render_template(
        'index.html',
        user=user,
        title='Wangyongxin',
        posts=posts,
    )

@app.route('/index')
def index():
    return 'hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requied for openid="' + form.openid.data + '",remember_me=' +str(form.remember_me.data))
        return redirect('/')
    return render_template(
        'login.html',
        title='sign in',
        form=form,
        providers = app.config('OPENID_PROVIDERS')
    )
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user
from app import app
from app.models.models import User
from app.alquimias import create_user

@app.route('/')
def index():
    posts = get_timeline() if current_user.is_authenticated else []
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Implementar lógica de login
    pass

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        foto = request.form['foto']
        bio = request.form['bio']
        create_user(username, email, password, foto, bio)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        body = request.form['body']
        create_post(body, current_user)
        return redirect(url_for('index'))
    return render_template('post.html')
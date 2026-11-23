import os

from flask import Flask, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

from database import Database

app = Flask(__name__)
db = None


def get_db():
    global db
    if db is None:
        db = Database(
            os.getenv('DB_HOST', 'localhost'),
            os.getenv('DB_USER', 'root'),
            os.getenv('DB_PASSWORD', 'admin'),
            os.getenv('DB_NAME', 'flask_auth'),
        )
    return db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    email = request.form.get('reg_email', '').strip()
    password = request.form.get('reg_pass', '')
    if not email or not password:
        return render_template('register.html', error='Заполните все поля')

    try:
        get_db().insert_users(email, generate_password_hash(password))
    except Exception:
        app.logger.exception('Registration failed')
        return render_template(
            'register.html',
            error='Не удалось зарегистрироваться. Проверьте подключение к MySQL и данные.',
        )
    return render_template('profile.html', class_name=email, places=None, error=None)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('log_name', '').strip()
    password = request.form.get('log_pass', '')
    if not email or not password:
        return render_template('login.html', error='Введите почту и пароль')

    try:
        user = get_db().select_users(email)
    except Exception:
        app.logger.exception('Login database query failed')
        return render_template(
            'login.html',
            error='Не удалось подключиться к базе данных. Проверьте настройки MySQL.',
        )

    if user:
        stored_password = user.get('password', '')
        if stored_password.startswith(('scrypt:', 'pbkdf2:')):
            password_ok = check_password_hash(stored_password, password)
        else:
            password_ok = stored_password == password
        if password_ok:
            return render_template(
                'profile.html', class_name=email, places=None, error=None
            )
    return render_template('login.html', error='Неверная почта или пароль')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

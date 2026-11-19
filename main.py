from flask import Flask, request, render_template, redirect, url_for

from database import Database


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('profile.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None


    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        try:
            if not username or not password:
                error = 'Заполните все поля'
            else:
                database = Database()
                user = database.get_user(username)

                if user and user['user_password'] == password:
                    return redirect(url_for('profile'))

                error = 'Неверное имя пользователя или пароль'

        except Exception as exception:
            error = f'Ошибка базы данных: {exception}'

    return render_template('login.html', error=error)


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
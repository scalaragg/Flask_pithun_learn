from flask import Flask, request, render_template, redirect, url_for

from database import get_teachers

app = Flask(__name__)

USERS = {
    "admin": "12345"
}


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
            elif username in USERS and USERS[username] == password:
                return redirect(url_for('index'))
            else:
                error = 'Неверное имя пользователя или пароль'

        except Exception:
            error = 'Ошибка при авторизации'

    return render_template('login.html', error=error)


@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('profile.html', person=username)


@app.route('/teachers')
def teachers():
    try:
        teachers_list = get_teachers()
        error = None
    except Exception as exception:
        teachers_list = []
        error = str(exception)

    return render_template(
        'teachers.html',
        teachers=teachers_list,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# PythonProject14

Flask-приложение с авторизацией по имени и просмотром преподавателей из базы данных `academy`.

## Запуск

```bash
pip install -r requirements.txt
python main.py
```

После запуска приложение доступно по адресу:

- http://127.0.0.1:8080/ — главная страница;
- http://127.0.0.1:8080/login — вход по имени;
- http://127.0.0.1:8080/teachers — список преподавателей из базы данных.

## База данных

Приложение подключается к MySQL:

- host: `localhost`
- user: `root`
- password: `admin`
- database: `academy`

Данные для страницы `/teachers` берутся из представления `v_select_teacher`.

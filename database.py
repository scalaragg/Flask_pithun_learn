import pymysql
import pymysql.cursors
import os

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        # Сначала подключаемся без указания базы, чтобы её создать
        self._create_database_if_not_exists()

        # Теперь подключаемся уже к нужной базе
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )

        # Создаём таблицы, если их ещё нет
        self._create_tables()

    def _create_database_if_not_exists(self):
        """Создаёт базу данных, если её нет"""
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset='utf8mb4',
        )
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"CREATE DATABASE IF NOT EXISTS `{self.database}` "
                    "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                )
            conn.commit()
        finally:
            conn.close()

    def _create_tables(self):
        """Создаёт нужные таблицы"""
        with self.connection.cursor() as cursor:
            # Таблица пользователей
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """)

            # Таблица классов (раз уж методы для неё есть)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS classes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    class_name VARCHAR(100) NOT NULL,
                    places INT NOT NULL DEFAULT 0
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
            """)
        self.connection.commit()

    def insert_users(self, email, password):
        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (email, password))
        self.connection.commit()

    def insert_classes(self, places1, places2):
        sql = "INSERT INTO classes (class_name, places) VALUES (%s, %s)"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (places1, places2))
        self.connection.commit()

    def select_classes(self):
        sql = "SELECT * FROM classes"
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def select_users(self, email):
        sql = "SELECT * FROM users WHERE email = %s"
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (email,))
            return cursor.fetchone()
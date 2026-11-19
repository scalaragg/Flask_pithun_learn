import mysql.connector


def get_teachers():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="academy"
        )

        cursor = connection.cursor()

        sql = "SELECT * FROM v_select_teacher"
        cursor.execute(sql)

        return cursor.fetchall()
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


if __name__ == "__main__":
    for row in get_teachers():
        print(row)

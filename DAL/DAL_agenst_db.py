import mysql.connector
class MainDAL:
    @staticmethod
    def connect(connection_string=None):
        if connection_string is None:
            connection_data = {
                "host": "localhost",
                "port": 3306,
                "user": "root",
                "password": "",
                "database": "eagleeyedb"
            }
        else:
            # אתה יכול לפתח פה אם תשתמש במחרוזת חיבור
            raise NotImplementedError("Custom connection strings not supported yet.")

        conn = mysql.connector.connect(**connection_data)
        return conn

    @staticmethod
    def disconnect(conn):
        conn.close()

    @staticmethod
    def execute(sql, connection_string=None):
        conn = MainDAL.connect(connection_string)
        cursor = conn.cursor(dictionary=True)  # מחזיר dict לפי שמות עמודות
        cursor.execute(sql)

        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def print_result(rows):
        if not rows:
            print("No results found.")
            return

        for row in rows:
            for key, value in row.items():
                print(f"{key}: {value}")
            print("---")

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
            raise NotImplementedError("Custom connection strings not supported yet.")

        conn = mysql.connector.connect(**connection_data)
        return conn

    @staticmethod
    def disconnect(conn):
        conn.close()

    @staticmethod
    def execute(sql, params=None, connection_string=None):
        conn = MainDAL.connect(connection_string)
        cursor = conn.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            if sql.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
            else:
                conn.commit()
                rows = None
        except Exception as e:
            print(f"Database error: {e}")
            rows = None
        finally:
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

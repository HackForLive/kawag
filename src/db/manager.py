import sqlite3
from sqlite3 import Error


class SqlLiteManager(object):
    def __init__(self, db_file):
        self._db_file = db_file
        self._notification_table_name = 'notifications'

    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self._db_file)
            print(sqlite3.version)
        except Error as error:
            print(error)
        finally:
            if conn:
                conn.close()

    def create_notification_table(self):
        conn = None

        try:
            conn = sqlite3.connect(self._db_file)

            # Create A Cursor
            cursor = conn.cursor()
            # Create A Table
            cursor.execute(f"""CREATE TABLE if not exists {self._notification_table_name}(
                name text)
            """)

            # Commit our changes
            conn.commit()
        except Error as error:
            print(error)
        finally:
            if conn:
                conn.close()

    def insert_new_record(self, notification):
        conn = None

        try:
            conn = sqlite3.connect(self._db_file)

            # Create A Cursor
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {self._notification_table_name} VALUES (:first)",
                    {
                        'first': notification,
                    }
                    )
            # Commit our changes
            conn.commit()
        except Error as error:
            print(error)
        finally:
            if conn:
                # Close our connection
                conn.close()

    def get_all_record(self):
        conn = None

        try:
            conn = sqlite3.connect(self._db_file)

            # Create A Cursor
            cursor = conn.cursor()
            # Grab records from database
            cursor.execute(f"SELECT * FROM {self._notification_table_name}")

            # Commit our changes
            conn.commit()
            return cursor.fetchall()
        except Error as error:
            print(error)
        finally:
            if conn:
                conn.close()
        return []

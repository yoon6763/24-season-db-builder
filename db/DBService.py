import os
import sqlite3


class DBService:
    def __init__(self):
        self.check_db_exist()

    def clear_db(self):
        conn = sqlite3.connect('db/season-24.db')
        print("Opened database successfully")
        conn.execute("DELETE FROM SEASON")
        conn.commit()
        print("Records deleted successfully")
        conn.close()

    def insert_season(self, season_response):
        conn = sqlite3.connect('db/season-24.db')
        conn.execute("INSERT INTO SEASON (NAME,YEAR,MONTH,DAY,HOUR,MINUTE) \
              VALUES (?,?,?,?,?,?)", (season_response.dateName, season_response.year, season_response.month,
                                      season_response.day, season_response.hour, season_response.minute))

        conn.commit()
        print("Data inserted successfully : ", season_response)
        conn.close()

    def create_db(self):
        # create db folder
        if not os.path.exists('db'):
            os.makedirs('db')

        # create db file
        conn = sqlite3.connect('db/season-24.db')
        print("Opened database successfully")
        conn.execute('''CREATE TABLE IF NOT EXISTS SEASON
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  NAME           TEXT    NOT NULL,
                  YEAR           TEXT    NOT NULL,
                    MONTH          TEXT    NOT NULL,
                    DAY          TEXT    NOT NULL,
                    HOUR          TEXT    NOT NULL,
                    MINUTE          TEXT    NOT NULL);''')
        print("Table created successfully")
        conn.close()

    def check_db_exist(self):
        # is db file exist?
        if not os.path.exists('db/season-24.db'):
            self.create_db()

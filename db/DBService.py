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


    def insert_season(self, season_info):
        conn = sqlite3.connect('db/season-24.db')
        conn.execute("INSERT INTO SEASON (NAME,YEAR,MONTH,DAY,HOUR,MINUTE) \
              VALUES (?,?,?,?,?,?)", (season_info.season, season_info.year, season_info.month,
                                      season_info.day, season_info.hour, season_info.minute))

        conn.commit()
        print("Data inserted successfully : ", season_info)
        conn.close()

    def create_db(self):
        # create db folder
        if not os.path.exists('db'):
            os.makedirs('db')

        # create db file
        conn = sqlite3.connect('db/season-24.db')
        print("Opened database successfully")
        conn.execute('''CREATE TABLE IF NOT EXISTS SEASON
               (NAME           TEXT    NOT NULL,
                  YEAR           INTEGER    NOT NULL,
                    MONTH          INTEGER    NOT NULL,
                    DAY          INTEGER    NOT NULL,
                    HOUR          INTEGER    NOT NULL,
                    MINUTE          INTEGER    NOT NULL);''')
        print("Table created successfully")
        conn.close()

    def check_db_exist(self):
        # is db file exist?
        if not os.path.exists('db/season-24.db'):
            self.create_db()

    def max_year_in_db(self):
        conn = sqlite3.connect('db/season-24.db')
        cursor = conn.execute("SELECT MAX(YEAR) FROM SEASON")
        max_year = cursor.fetchone()[0]
        conn.close()
        return max_year
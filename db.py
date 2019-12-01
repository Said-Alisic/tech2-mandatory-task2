from flask import Flask
from flask_mysqldb import MySQL


class db_connection:
    
    def connect_to_db(self, app):
        app = app

    # initialize MySQl - now we can create a cursor and execute queries
        mysql = MySQL(app)

    # Config MySQL
        app.config["MYSQL_HOST"] = "localhost"
        app.config["MYSQL_USER"] = "root"
        app.config["MYSQL_PASSWORD"] = "Dunno11pass"
        app.config["MYSQL_DB"] = "icar"

        return mysql


    def get_cars(self, mysql):
            # create cursor to be able to query the db
            cur = mysql.connection.cursor()

            cur.execute("SELECT * FROM cars")

            cars = list(cur.fetchall())

            cur.close()

            return cars


from flask import Flask
from flask_mysqldb import MySQL


class db_connection:
    
    def connect_to_db(self, app):
        app = app

    # initialize MySQl - now we can create a cursor and execute queries
        mysql = MySQL(app)

    # Config MySQL
        app.config["MYSQL_HOST"] = "tech2.c1kmakec5tit.us-east-2.rds.amazonaws.com"
        app.config["MYSQL_USER"] = "tech2"
        app.config["MYSQL_PASSWORD"] = "tech2-password"
        app.config["MYSQL_DB"] = "tech2"
    
    # Locally
    #    app.config["MYSQL_HOST"] = "localhost"
    #    app.config["MYSQL_USER"] = "root"
    #    app.config["MYSQL_PASSWORD"] = "Dunno11pass"
    #    app.config["MYSQL_DB"] = "said_dev"

    # For calling methods to execute queries - specifying a cursor type
        app.config["MYSQL_CURSORCLASS"] = "DictCursor"   

        return mysql


    def get_songs(self, mysql):
            # create cursor to be able to query the db
            cur = mysql.connection.cursor()

            cur.execute("SELECT * FROM songs")

            songs = cur.fetchall()

            cur.close()

            return songs


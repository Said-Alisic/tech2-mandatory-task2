from flask import Flask
from flask_mysqldb import MySQL


class db_connection:
    
    def connect_to_db(self, app):
        app = app

    # initialize MySQl - now we can create a cursor and execute queries
        mysql = MySQL(app)

    # Config MySQL
        app.config["MYSQL_HOST"] = "sql2.freemysqlhosting.net"
        app.config["MYSQL_USER"] = "sql2314040"
        app.config["MYSQL_PASSWORD"] = "zM1!lP5%"
        app.config["MYSQL_DB"] = "sql2314040"
    
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


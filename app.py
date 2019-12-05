from flask import Flask, jsonify, render_template
from db import db_connection

app = Flask(__name__)

db = db_connection()
connection = db.connect_to_db(app)


@app.route('/songs')
def get_songs():

    songs = db.get_songs(connection)
    print(songs)

    return render_template("songs.html", songs=songs)
    

@app.route('/')
def home():

    return render_template("home.html")


if __name__ == "__main__":
    print('Flask app is running...')
    app.run('0.0.0.0', '8080')
    print('...Flask app has stopped.')


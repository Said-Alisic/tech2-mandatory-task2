from flask import Flask, jsonify
from db import db_connection

app = Flask(__name__)

db = db_connection()
connection = db.connect_to_db(app)

@app.route('/cars')
def get_cars():

    cars = db.get_cars(connection)

    return jsonify({'cars' : cars})
    


if __name__ == "__main__":
    print('Flask app is running...')
    app.run()
    print('...Flask app has stopped.')


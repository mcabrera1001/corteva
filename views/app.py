from flask import jsonify, Flask
from models import Weather

from config.flask_and_database import db, app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/weather", methods=['GET'])
def get_weather():
    print(Weather.query.all())
    return jsonify(Weather.query.first())
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)

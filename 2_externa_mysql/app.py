import flask
from flask import request, json, jsonify
import requests
import flask_mysqldb
from flask import Flask
from flask_mysqldb import MySQL

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = "host.docker.internal" # to access the local machine hosting docker
app.config['MYSQL_USER'] = "root"
app.config['MYSQ_PASSWORD'] = "root"
app.config['MYSQ_PORT'] = "3306"
app.config['MYSQL_DB'] = "flaskhost"

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route("/inserthost", methods=['POST'])
def inserthost():
    data = requests.get('https://randomuser.me/api').json()
    username = data['results'][0]['name']['first']
    query = "INSERT INTO users(name) VALUES(%s)".format(username)
    curl = mysql.connection.cursor()
    curl.execute(query)
    mysql.connection.commit()
    curl.close()
    return username


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5002")
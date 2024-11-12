import os
from flask import Flask, request, jsonify, make_response
import socket
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Initialize global counter
counter = 0

# MySQL configuration
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'mysql',
    'database': 'app_db'
}

# Create a MySQL connection
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def index():
    global counter
    counter += 1

    # Get internal IP of the container
    internal_ip = socket.gethostbyname(socket.gethostname())

    # Create a cookie with the internal IP that lasts for 5 minutes
    resp = make_response(jsonify({"message": "Counter incremented", "internal_ip": internal_ip}))
    resp.set_cookie('server_ip', internal_ip, max_age=300)  # 5 minutes cookie

    # Log the request in the MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS access_log (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            client_ip VARCHAR(255),
            internal_ip VARCHAR(255)
        )
    """)
    cursor.execute("""
        INSERT INTO access_log (timestamp, client_ip, internal_ip)
        VALUES (%s, %s, %s)
    """, (datetime.now(), request.remote_addr, internal_ip))
    conn.commit()
    cursor.close()
    conn.close()

    return resp

@app.route('/showcount')
def showcount():
    return jsonify({"counter": counter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

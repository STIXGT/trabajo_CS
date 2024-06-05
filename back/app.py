# app.py
from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config
from routes import init_routes

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar MySQL
mysql = MySQL(app)

# Inicializar CORS
CORS(app)

# Inicializar rutas
init_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True)

import json, requests, datetime, time
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config.Config')

api = Api(app)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app.modules.serverinfo import ServerInfo, ServerInfoResource

api.add_resource(ServerInfoResource, '/api/servers/')

@app.route('/')
def index():
    return render_template('index.html')

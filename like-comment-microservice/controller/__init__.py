from flask import Flask
from flask_cors import CORS

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 0
}

app = Flask(__name__)
CORS(app)

from controller import request_controller

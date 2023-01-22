import os
from datetime import datetime

from bson import ObjectId, json_util
from flask import Flask
from flask.json import JSONEncoder

from core.views import core
from globals import db, login_manager
from users.views import users


class MongoJsonEncoder(JSONEncoder):
    """Adjustments to the Flask json encoder for MongoEngine support"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    """Create the flask application"""

    # Initiate app
    app = Flask(__name__)
    app.json_encoder = MongoJsonEncoder

    # Update app.config from environment variables
    app.config["SECRET_KEY"] ='StockPricePredictionS' 
    app.config["MONGODB_SETTINGS"] = {
        "authentication_source": "admin",
        "host":'mongodb+srv://Fintech:qANVTzWevwD9UZz6@stockpriceprediction.9srtpdu.mongodb.net/?retryWrites=true&w=majority' ,
        "port":27017 ,
        "username":'Fintech',
        "password":'qANVTzWevwD9UZz6'
    }

    # register blueprints
    app.register_blueprint(core, url_prefix="")
    app.register_blueprint(users, url_prefix="/users")

    # initialize database
    db.init_app(app)

    # initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    return app

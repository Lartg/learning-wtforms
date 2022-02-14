from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
from flask_login import LoginManager
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)
flask_bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
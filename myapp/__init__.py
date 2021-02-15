"""Ce module est responsable d'initialiser l'application."""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
environment = os.getenv('FLASK_ENV')
app.config.from_object(f'config.{environment}')
db = SQLAlchemy(app)

from . import views
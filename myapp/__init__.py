"""Ce module est responsable d'initialiser l'application."""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
environment = os.getenv('FLASK_ENV')
app.config.from_object(f'config.{environment}')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
from . import models
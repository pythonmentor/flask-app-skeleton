"""Ce module est responsable d'initialiser l'application."""

from flask import Flask

app = Flask(__name__)

from . import views
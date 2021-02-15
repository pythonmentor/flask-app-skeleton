"""Fichier de configuration de l'app myapp."""

import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = (
    os.getenv('DATABASE_URL') or f'sqlite:///{BASE_DIR}/db.sqlite3'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
"""Fichier de configuration de l'app myapp."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = BASE_DIR / f'{os.getenv("FLASK_APP")}'
CONFIG_DIR = BASE_DIR / 'config'
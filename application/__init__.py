from flask import Flask
import os
from dotenv import load_dotenv

from pathlib import Path
envpath = Path('.') / 'application'
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/uploads/')

from application.core.views import core
app.register_blueprint(core, url_prefix="/")

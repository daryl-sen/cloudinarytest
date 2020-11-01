from flask import Flask
from dotenv import load_dotenv

from dotenv import load_dotenv
import os

load_dotenv()

cloudinary_vars = {
    'CLOUDINARY_NAME': os.getenv('CLOUDINARY_NAME'), 
    'CLOUDINARY_API_KEY': os.getenv('CLOUDINARY_API_KEY'), 
    'CLOUDINARY_API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}

# inside .env
# export SECRET_KEY=value
# export CLOUDINARY_API_KEY=value
# export CLOUDINARY_API_SECRET=value
# export CLOUDINARY_NAME=value

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/uploads/')

from application.core.views import core
app.register_blueprint(core, url_prefix="/")

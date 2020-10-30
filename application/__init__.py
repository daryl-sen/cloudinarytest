from flask import Flask
from dotenv import load_dotenv
import os
import cloudinary as cloud

load_dotenv()

cloud.config.update = ({
    'cloud_name':os.getenv('CLOUDINARY_CLOUD_NAME'),
    'api_key': os.getenv('CLOUDINARY_API_KEY'),
    'api_secret': os.getenv('CLOUDINARY_API_SECRET')
})

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from application.core.views import core
app.register_blueprint(core, url_prefix="/")

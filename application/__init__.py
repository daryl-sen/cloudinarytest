from flask import Flask
from dotenv import load_dotenv

from dotenv import load_dotenv
import os
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
load_dotenv()

cloudinary_vars = {
    'CLOUDINARY_NAME': os.getenv('CLOUDINARY_NAME'), 
    'CLOUDINARY_API_KEY': os.getenv('CLOUDINARY_API_KEY'), 
    'CLOUDINARY_API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}

# cloudinary.config( 
#   cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'), 
#   api_key = os.getenv('CLOUDINARY_API_KEY'), 
#   api_secret = os.getenv('CLOUDINARY_API_SECRET')
# )

# print('key')
# print(os.getenv('CLOUDINARY_API_KEY'))
# print(cloudinary_vars['CLOUDINARY_CLOUD_NAME'])

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/uploads/')

from application.core.views import core
app.register_blueprint(core, url_prefix="/")

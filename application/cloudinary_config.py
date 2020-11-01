from dotenv import load_dotenv
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

cloudinary_vars = {
    'CLOUDINARY_NAME': os.getenv('CLOUDINARY_NAME'), 
    'CLOUDINARY_API_KEY': os.getenv('CLOUDINARY_API_KEY'), 
    'CLOUDINARY_API_SECRET': os.getenv('CLOUDINARY_API_SECRET')
}

cloudinary.config( 
    cloud_name = os.getenv('CLOUDINARY_NAME'), 
    api_key = os.getenv('CLOUDINARY_API_KEY'), 
    api_secret = os.getenv('CLOUDINARY_API_SECRET')
)

def upload_to_cloudinary(image):
    status = cloudinary.uploader.upload(image)
    return status['secure_url']




# inside .env, which should be placed in the same folder as this .py file
# export SECRET_KEY=value
# export CLOUDINARY_API_KEY=value
# export CLOUDINARY_API_SECRET=value
# export CLOUDINARY_NAME=value
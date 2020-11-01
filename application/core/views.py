from flask import render_template, Blueprint, redirect, url_for, flash, request
from application.core.forms import *
from application import app, basedir, cloudinary_vars

import cloudinary
import cloudinary.uploader
import cloudinary.api
core = Blueprint('core', __name__, template_folder = 'templates/core')


@core.route('/', methods=['get','post'])
def index():
    form = upload_form()
    if form.validate_on_submit():

        cloudinary.config( 
          cloud_name = cloudinary_vars['CLOUDINARY_NAME'], 
          api_key = cloudinary_vars['CLOUDINARY_API_KEY'], 
          api_secret = cloudinary_vars['CLOUDINARY_API_SECRET']
        )


        f = form.file.data
        print(f.filename)
        cloudinary.uploader.upload(f)
        # f.save(app.config['UPLOAD_FOLDER'], 'image.jpg')
        return redirect(url_for('core.index'))
    return render_template('index.html', form = form)

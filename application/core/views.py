from flask import render_template, Blueprint, redirect, url_for, flash, request
from application.core.forms import *
from application import app, basedir
from application.cloudinary_config import upload_to_cloudinary

core = Blueprint('core', __name__, template_folder = 'templates/core')


@core.route('/', methods=['get','post'])
def index():
    form = upload_form()
    if form.validate_on_submit():

        f = form.file.data
        print(upload_to_cloudinary(f))

        return redirect(url_for('core.index'))
    return render_template('index.html', form = form)

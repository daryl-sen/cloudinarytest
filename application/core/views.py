from flask import render_template, Blueprint, redirect, url_for, flash, request
from application.core.forms import *

core = Blueprint('core', __name__, template_folder = 'templates/core')


@core.route('/')
def index():
    form = upload_form()
    return render_template('index.html', form = form)

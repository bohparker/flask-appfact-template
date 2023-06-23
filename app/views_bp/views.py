from flask import render_template
from . import views_bp as bp


@bp.route('/')
def index():
    return render_template('index.html')
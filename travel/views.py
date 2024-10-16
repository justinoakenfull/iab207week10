from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db
from sqlalchemy.sql import func

mainbp = Blueprint('main', __name__)

@mainbp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destination_id = request.form.get('destination_id')
        return redirect(url_for('destination.show', id=destination_id))
    destinations = db.session.execute(db.select(Destination)).scalars()
    top_destinations = db.session.scalars(db.select(Destination).order_by(func.random()).limit(3))
    return render_template('index.html', destinations=destinations, top_destinations=top_destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        top_destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        destinations = db.session.execute(db.select(Destination)).scalars()
        return render_template('index.html', destinations=destinations, top_destinations=top_destinations)
    else:
        return redirect(url_for('main.index'))

from flask import Blueprint, render_template, redirect, url_for, flash, abort
from .models import Destination, Comment, User
from .forms import DestinationForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask import current_app as app
from flask_login import login_required, current_user

destinationBlueprint = Blueprint('destination', __name__, url_prefix='/destinations')

@destinationBlueprint.route('/<id>')
def show(id):
    print("Destination Page")
    commentForm = CommentForm()
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    return render_template('destinations/show.html', destination=destination, form=commentForm)

@destinationBlueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    print("Create Destination")
    form = DestinationForm()
    if form.validate_on_submit():
        file_path = check_file_upload(form)
        destination = Destination(name = form.name.data, 
                                  description = form.description.data, 
                                  image = file_path, 
                                  currency = form.currency.data)
        db.session.add(destination)
        db.session.commit()
        flash('Successfully created new travel destination', 'success')
        return redirect(url_for('destination.create'))

    return render_template('destinations/create.html', form=form)
    
@destinationBlueprint.route('/<id>/comment', methods=['GET','POST'])
@login_required
def comment(id):
    form = CommentForm()  
    # get the destination object associated to the page and the comment
    destination = db.session.scalar(db.select(Destination).where(Destination.id==id))
    if form.validate_on_submit():  
      # read the comment from the form
      comment = Comment(text=form.comment.data, destination=destination, user=current_user) 
      # here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 
      # flashing a message which needs to be handled by the html
      flash('Your comment has been added', 'success')  
      # print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=id))

def check_file_upload(form):
    file_data = form.image.data
    filename = secure_filename(file_data.filename)
    BASE_PATH = os.path.dirname(__file__)
    UPLOAD_PATH = os.path.join(BASE_PATH, 'static/image', filename)
    print(UPLOAD_PATH)
    db_upload_path = f'/static/image/{filename}'
    file_data.save(UPLOAD_PATH)
    return db_upload_path

def get_destination(id):
    # create a destription of brazil
    b_desc = "Brazil is a country of contrasts. It's famous for its carnival, its music, its dance, and its football. It's a country of great wealth and great poverty, and its people are as diverse as its geography."
    image_loc = ""
    currency = "R$10"
    brazil = Destination(1,"Brazil", b_desc, image_loc, currency)
    comment = Comment("John", "This is a great place to visit", "2020-01-01")
    brazil.set_comments(comment)
    comment = Comment("Alice", "The food is amazing, and the people are friendly", "2020-01-02")
    brazil.set_comments(comment)
    comment = Comment("Bob", "I loved the beaches and the weather", "2020-01-03")
    brazil.set_comments(comment)
    comment = Comment("Charlie", "I didn't like the food, but the music was great", "2020-01-04")
    brazil.set_comments(comment)
    comment = Comment("David", "The culture is rich and vibrant", "2020-01-05")
    brazil.set_comments(comment)

    # create a description of another country
    c_desc = "Canada is known for its stunning natural landscapes, including the Rocky Mountains and Niagara Falls. It is also famous for its maple syrup, ice hockey, and friendly people."
    image_loc = ""
    currency = "CAD$11"
    canada = Destination(2,"Canada", c_desc, image_loc, currency)
    comment = Comment("John", "I loved exploring Banff National Park", "2020-02-01")
    canada.set_comments(comment)
    comment = Comment("Alice", "The poutine is a must-try", "2020-02-02")
    canada.set_comments(comment)
    comment = Comment("Bob", "I enjoyed skiing in Whistler", "2020-02-03")
    canada.set_comments(comment)

    # create a description of another country
    f_desc = "France is known for its rich history, art, and cuisine. It is home to iconic landmarks such as the Eiffel Tower and the Louvre Museum."
    image_loc = ""
    currency = "EUR€100"
    france = Destination(3,"France", f_desc, image_loc, currency)
    comment = Comment("John", "Paris is a beautiful city", "2020-03-01")
    france.set_comments(comment)
    comment = Comment("Alice", "The croissants are delicious", "2020-03-02")
    france.set_comments(comment)
    comment = Comment("Bob", "I enjoyed visiting the Palace of Versailles", "2020-03-03")
    france.set_comments(comment)

    # create a description of another country
    j_desc = "Japan is a country of ancient traditions and modern technology. It is famous for its cherry blossoms, sushi, and bullet trains."
    image_loc = ""
    currency = "JPN¥1000"
    japan = Destination(4,"Japan", j_desc, image_loc, currency)
    comment = Comment("John", "Kyoto is a must-visit city", "2020-04-01")
    japan.set_comments(comment)
    comment = Comment("Alice", "I loved exploring Tokyo", "2020-04-02")
    japan.set_comments(comment)
    comment = Comment("Bob", "The hot springs in Hakone were amazing", "2020-04-03")
    japan.set_comments(comment)

    # add the countries to a list
    countries = [brazil, canada, france, japan]
    if int(id) < 0 or int(id) >= len(countries):
        return brazil
    foundCountry = countries[int(id)]

    if foundCountry != None:
        return foundCountry
    else:
        return brazil
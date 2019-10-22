import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_review'
app.config["MONGO_URI"] = env.MONGO_URI


mongo = PyMongo(app)

@app.route('/')
@app.route('/ get_comments')
def get_comments():
    return render_template("bookdetails.html", comments=mongo.db.comments.find())

@app.route('/book_info/<book_id>')
def book_info(book_id):
    the_book = mongo.db.book_details.find_one({"_id": ObjectId(book_id)})
    all_categories = mongo.db.categories.find()
    return render_template('bookdetails.html', book=the_book, categories=all_categories, comments=mongo.db.comments.find())








@app.route('/ search', methods= ['GET'])
def search(book_id):
        the_book = mongo.db.book_details.find({"Title"})
        all_categories = mongo.db.categories.find()
        return render_template('search.html', book=the_book, categories=all_categories)
        
        
        
        
        
    {% for book in books%} {% if book in search %}
    <div class="collection">
        <a href="{{url_for( 'book_info', book_id=book._id)}} " class="collection-item"> {{book.Title}}</a>
    </div>
    {% endif %} {% endfor %}

        
        

@app.route('/comments/<comment_id>')
def comments(comment_id):
    the_comment = mongo.db.comments({"_id": ObjectId(comment_id)})
    all_categories = mongo.db.categories.find()
    return render_template('bookdetails.html', comment=the_comment, categories=all_categories)

    
#  takes the details from the form and adds the comment to the database, then redirects to bookdetails page 
@app.route('/insert_comment', methods=['POST'])
def insert_comment():
    
    new_comment = {
        'comment': request.form.get('comments'),
    }
    
    comments = mongo.db.comments
    comments.insert_one(new_comment)
    # ----- get comments should be book.details page to display that the comment just added is present
    return redirect(url_for('get_comments'))








# might be useufl

#  takes the details from the form and adds the comment to the database, then redirects to bookdetails page 
@app.route('/insert_comment', methods=['POST'])
def insert_comment():
    
    new_comment = {
        'comment': request.form.get('comments'),
    }
    
    comments = mongo.db.comments
    comments.insert_one(new_comment)
    # ----- get comments should be book.details page to display that the comment just added is present
    return redirect(url_for('get_comments'))
    
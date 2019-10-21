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
@app.route('/ get_books')
def get_books():
     return render_template("books.html", books=mongo.db.book_details.find())


@app.route('/edit_book/<book_id>')
def edit_book(book_id):
    the_book = mongo.db.book_details.find_one({"_id": ObjectId(book_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editbook.html', book=the_book, categories=all_categories)

@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    books = mongo.db.book_details
    books.update( {'_id': ObjectId(book_id)},
    {
        'Title': request.form.get('Title'),
        'Author': request.form.get('Author'),
        'Genre': request.form.get('Genre'),
        'Year': request.form.get('Year'),
        'Image_URL': request.form.get('Image_URL'),
        'Amazon': request.form.get('Amazon'),
        'Review': request.form.get('Review')
    })
    return redirect(url_for('get_books'))

#book details page 
@app.route('/book_info/<book_id>')
def book_info(book_id):
    the_book = mongo.db.book_details.find_one({"_id": ObjectId(book_id)})
    all_categories = mongo.db.categories.find()
    return render_template('bookdetails.html', book=the_book, categories=all_categories)

def get_comments():
     return render_template('bookdetails.html', comments=mongo.db.comments.find())

#  takes the details from the form and adds the comment to the database, then redirects to bookdetails page 

@app.route('/insert_comment', methods=['POST'])
def insert_comment():
    
    new_comment = {
        'bookID': request.form.get('bookID'),
        'comment': request.form.get('comment')
    }
    comments = mongo.db.comments
    comments.insert_one(new_comment)
    # ----- get comments should be book.details page to display that the comment just added is present
    return  redirect(url_for('get_books'))
    
# displays add books page
@app.route('/add_book')
def add_book():
    return render_template('addbook.html')

#  takes the details from the form and adds the book to the database, then redirects to home page 
@app.route('/insert_book', methods=['POST'])
def insert_book():
    
    new_book = {
        'Title': request.form.get('Title'),
        'Author': request.form.get('Author'),
        'Genre': request.form.get('Genre'),
        'Year': request.form.get('Year'),
        'Image_URL': request.form.get('Image_URL'),
        'Amazon': request.form.get('Amazon'),
        'Review': request.form.get('Review'),
        'upvotes': 0,
    }
    
    books = mongo.db.book_details
    books.insert_one(new_book)
    # ----- get books should be home page to display that the book just added is present
    return redirect(url_for('get_books'))
    
# delete the book
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.book_details.remove({'_id': ObjectId(book_id)})
    return redirect(url_for('get_books'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
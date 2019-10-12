import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_review'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)

@app.route('/')
@app.route('/ get_books')
def get_books():
     return render_template("books.html", books=mongo.db.book_details.find())

@app.route('/edit_book/ <book_id')
def edit_book(book_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editbook.html', book=the_book, categories=all_categories)

@app.route('/update_book/<book_id>', method=["POST"])
def update_book(book_id):
    books = mongo.db.books
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
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


# displays add books page

@app.route('/add_book')
def add_book():
    return render_template('addbook.html')

#  takes the details from the form and adds the book to the database, then redirects to home page 
@app.route('/insert_book', methods=['POST'])
def insert_book():
    # - ------- check if it should be books or book
    books = mongo.db.books
    books.insert_one(request.form.to_dict())
    # ----- get books should be home page to display that het book just added is present
    return redirect(url_for('get_books'))
    
    
{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":34},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId"],"id":1}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":21},"action":"insert","lines":["app = Flask(__name__)"],"id":3}],[{"start":{"row":5,"column":21},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":20,"column":15},"action":"insert","lines":["mongo = PyMongo(app)","","@app.route('/')","@app.route('/ get_books')","def get_books():","     return render_template(\"books.html\", books=mongo.db.book_details.find())","","","if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","    port=int(os.environ.get('PORT')),","    debug=True)"],"id":5}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":7,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["app.config[\"MONGO_DBNAME\"] = 'book_review'","app.config[\"MONGO_URI\"] = 'mongodb+srv://root:PASSWORD@myfirstcluster-mi7s3.mongodb.net/book_review?retryWrites=true&w=majority'",""],"id":7}],[{"start":{"row":8,"column":128},"end":{"row":9,"column":0},"action":"remove","lines":["",""],"id":8}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":54},"action":"remove","lines":["PASSWORD"],"id":9},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["M"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["o"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["n"]}],[{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"remove","lines":["n"],"id":10},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"remove","lines":["o"]},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"remove","lines":["M"]}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["m"],"id":11},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["o"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["n"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["g"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["o"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["D"]}],[{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["B"],"id":12},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["1"]},{"start":{"row":8,"column":54},"end":{"row":8,"column":55},"action":"insert","lines":["2"]},{"start":{"row":8,"column":55},"end":{"row":8,"column":56},"action":"insert","lines":["3"]}],[{"start":{"row":8,"column":46},"end":{"row":8,"column":56},"action":"remove","lines":["mongoDB123"],"id":13},{"start":{"row":8,"column":46},"end":{"row":8,"column":47},"action":"insert","lines":["P"]},{"start":{"row":8,"column":47},"end":{"row":8,"column":48},"action":"insert","lines":["A"]},{"start":{"row":8,"column":48},"end":{"row":8,"column":49},"action":"insert","lines":["S"]},{"start":{"row":8,"column":49},"end":{"row":8,"column":50},"action":"insert","lines":["S"]},{"start":{"row":8,"column":50},"end":{"row":8,"column":51},"action":"insert","lines":["W"]},{"start":{"row":8,"column":51},"end":{"row":8,"column":52},"action":"insert","lines":["O"]},{"start":{"row":8,"column":52},"end":{"row":8,"column":53},"action":"insert","lines":["R"]},{"start":{"row":8,"column":53},"end":{"row":8,"column":54},"action":"insert","lines":["D"]}],[{"start":{"row":22,"column":15},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":15},{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"remove","lines":["",""]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":24,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":25,"column":0},"end":{"row":36,"column":126},"action":"insert","lines":["# displays add books page","","# @app.route('/add_book')","# def add_book():","# return render_template('addbook.html')","","#  takes the details from the form and adds the book to the database, then redirects to home page ","# @app.route('/insert_book', methods=['POST'])","# def insert_book():","#     books = mongo.db.books - ------- check if it should be books or book","#     books.insert_one(request.form.to_dict())","#     return redierct(url_for('get_books')) ----- get books should be home page to display that het book just added is present"],"id":17}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"remove","lines":["# "],"id":18},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"remove","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"remove","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"remove","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"remove","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"remove","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"remove","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"remove","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"remove","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "],"id":19}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "],"id":20}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":21}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":6},"action":"insert","lines":["# "],"id":22}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"remove","lines":["#"],"id":23},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "],"id":24}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":5},"action":"remove","lines":[" "],"id":25}],[{"start":{"row":34,"column":27},"end":{"row":34,"column":72},"action":"remove","lines":["- ------- check if it should be books or book"],"id":26}],[{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"remove","lines":[" "],"id":27}],[{"start":{"row":33,"column":18},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":49},"action":"insert","lines":["- ------- check if it should be books or book"],"id":29}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":6},"action":"insert","lines":["# "],"id":30}],[{"start":{"row":37,"column":41},"end":{"row":37,"column":124},"action":"remove","lines":[" ----- get books should be home page to display that het book just added is present"],"id":31}],[{"start":{"row":36,"column":44},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":6},"action":"insert","lines":["# "],"id":33}],[{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":[" "],"id":34}],[{"start":{"row":37,"column":5},"end":{"row":37,"column":88},"action":"insert","lines":[" ----- get books should be home page to display that het book just added is present"],"id":35}],[{"start":{"row":38,"column":11},"end":{"row":38,"column":19},"action":"remove","lines":["redierct"],"id":36},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["r"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["e"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["d"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["i"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["r"]},{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"insert","lines":["e"]},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"insert","lines":["c"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":218.5,"scrollleft":0,"selection":{"start":{"row":38,"column":41},"end":{"row":38,"column":41},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1570871966639,"hash":"296362839001c8a472e2516798fd624db5a72d78"}
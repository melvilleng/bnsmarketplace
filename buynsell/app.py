from flask import Flask, render_template, request, redirect, url_for,session, flash
import pymongo
import os
import datetime
from bson.objectid import ObjectId
import sys
from dotenv import load_dotenv
load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
DB_NAME = "carousell"

# create the flask app and set the session
app = Flask(__name__)



@app.route('/show_product')
def show_product():
    all_product = client[DB_NAME].carousell.find()
    return render_template('show_product.template.html', result = all_product)

@app.route('/create_listing')
def listing_product():
    return render_template('create_listing.template.html')

@app.route('/create_listing', methods=['POST'])
def process_create_listing():
    client.carousell.carousell.insert_one({
        "name": request.form.get("name"),
        "price": request.form.get("price"),
        "description": request.form.get("description"),
        "date": datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d"),
        "email": request.form.get("email"),
        "username": request.form.get("username"),
        "userid" : ObjectId()

    })
    return redirect(url_for("show_product"))



@app.route('/edit_listing/<product_id>')
def show_editing_product(product_id):
    product = client[DB_NAME].carousell.find_one({
        "_id": ObjectId(product_id)
    })
    return render_template('edit_listing.template.html', product= product)

@app.route('/edit_listing/<product_id>', methods=["POST"])
def process_edit_product(product_id):
    client[DB_NAME].carousell.update_one({
        "_id": ObjectId(product_id)
    },{
        "$set": {
                "name":request.form.get("name"),
                "price":request.form.get("price"),
                "description":request.form.get("description")
        }
    })
    return redirect(url_for('show_product'))

@app.route('/delete_listing/<product_id>')
def delete_listing(product_id):
    client[DB_NAME].carousell.remove({'_id': ObjectId(product_id)})
    return redirect(url_for("show_product"))

@app.route('/display_listing/<product_id>')
def display_listing(product_id):
    product = client[DB_NAME].carousell.find({
        "_id": ObjectId(product_id)
    },{
        'name': 1 , 'price' : 1
    })
    return render_template('display_listing.template.html', product= product)







# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
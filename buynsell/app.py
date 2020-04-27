from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from bson.objectid import ObjectId
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
    return render_template('listing.template.html')

@app.route('/create_listing', methods=['POST'])
def process_edit_listing_product():
    client.carousell.carousell.insert_one({
        "Name":request.form.get("name"),
        "Price":request.form.get("price"),
        "Description":request.form.get("description")

    })
    return "added"


@app.route('/edit_listing/<product_id>')
def show_editing_product(product_id):
    product = client[DB_NAME].carousell.find_one({
        "_id": ObjectId(product_id)
    })
    return render_template('edit_listing.template.html', product= product)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
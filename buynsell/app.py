from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
import datetime
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
def process_create_listing():
    client.carousell.carousell.insert_one({
        "Name": request.form.get("name"),
        "Price": request.form.get("price"),
        "Description": request.form.get("description"),
        "date": datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d"),
        "email": request.form.get("email"),
        "username": request.form.get("username")

    })
    return redirect(url_for("userproduct"))


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
                "Name":request.form.get("name"),
                "Price":request.form.get("price"),
                "Description":request.form.get("description")
        }
    })
    return redirect(url_for("show_product"))

@app.route('/delete_listing/<product_id>')
def delete_listing(product_id):
    client[DB_NAME].carousell.remove({'_id': ObjectId(product_id)})
    return redirect(url_for("show_product"))

@app.route('/show_user')
def show_user():
    all_user= client[DB_NAME].user.find()
    return render_template('show_user.template.html', user = all_user)

@app.route('/create_user')
def show_create_user():
    return render_template('create_user.template.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    new_user = client[DB_NAME].user.insert_one({
        "username":request.form.get("username"),
        "email":request.form.get("email"),

    })
    return render_template('userproduct.template.html')






# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
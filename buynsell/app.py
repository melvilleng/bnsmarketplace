from flask import Flask, render_template, request, redirect, url_for,session, flash
import pymongo
import os
import datetime
from bson.objectid import ObjectId
import sys
from dotenv import load_dotenv
from passlib.hash import pbkdf2_sha256
import flask_login
load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
DB_NAME = "carousell"


# create the flask app and set the session
app = Flask(__name__)
app.secret_key= os.environ.get("SECRET_KEY")

login_manager = flask_login.LoginManager()
login_manager.init_app(app)




class User(flask_login.UserMixin):
    pass

def encrypt_password(plaintext):
    return pbkdf2_sha256.hash(plaintext)

def verify_password(plaintext,encrypted):
    return pbkdf2_sha256.verify(encrypted,plaintext)

@login_manager.user_loader
def user_loader(username):
    user = client[DB_NAME].user.find_one({
        "username": username
    })

    login_user = User()
    login_user.id = user['username']
    return login_user

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
        "username": request.form.get("username")

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


@app.route('/login')
def login():
    return render_template('login.template.html')

@app.route('/login',methods=['POST'])
def signing_in():
    username = request.form.get('username')
    password = request.form.get('password')

    user = client[DB_NAME].user.find_one({
        'username':username
    }) 

    if user and verify_password(user['password'],password):
        login_user = User()
        login_user.id = user['username']
        flask_login.login_user(login_user)
        return "logged"
    else:
        return "logged fail"

@app.route('/create_user')
def signup():
    return render_template('signup.template.html')

@app.route('/create_user',methods=["POST"])
def creating_user():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    current_user= client[DB_NAME].user.find_one({
        'username':username
    })
    if current_user:
        return "Email in database"

    client[DB_NAME].user.insert_one({
        'username':username,
        'email':email,
        'password':encrypt_password(password)
    })
    return "done"

@app.route('/profile_product')
@flask_login.login_required   
def private_section():
    return "one product" + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return "logged out"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/create_listing/<userid>')
def listing_product(userid):
    return render_template('create_listing.template.html')

@app.route('/create_listing/<userid>', methods=['POST'])
def process_create_listing(userid):
    client.carousell.carousell.insert_one({
        "userid":ObjectId(userid),
        "name": request.form.get("name"),
        "price": request.form.get("price"),
        "description": request.form.get("description"),
        "date": datetime.datetime.strptime(request.form.get('date'), "%Y-%m-%d"),
        "created_by":flask_login.current_user.id

    })
    return redirect(url_for("private_section"))



@app.route('/edit_listing/<product_id>/<userid>')
def show_editing_product(product_id,userid):
    product = client[DB_NAME].carousell.find_one({
        "_id": ObjectId(product_id),
        "userid":ObjectId(userid)
    })
    return render_template('edit_listing.template.html', product= product,userid=userid)

@app.route('/edit_listing/<product_id>/<userid>', methods=["POST"])
def process_edit_product(product_id,userid):
    
    
    client[DB_NAME].carousell.update_one({
        "_id": ObjectId(product_id)
    },{
        "$set": {
                "name":request.form.get("name"),
                "price":request.form.get("price"),
                "description":request.form.get("description")
        }
    })
    return redirect(url_for('listing',product_id=product_id,userid=userid))

# @app.route('/listing/<userid>')
# def listing(userid):
#     product_post = client[DB_NAME].carousell.find({
#         'userid':ObjectId(userid)
#     })
#     return render_template('productpost.template.html',product_post = product_post)


@app.route('/delete_listing/<product_id>/<userid>')
def delete_listing(product_id,userid):
    client[DB_NAME].carousell.remove({
        "_id": ObjectId(product_id),
        "userid":ObjectId(userid)
    })
    return redirect(url_for('listing',product_id=product_id,userid=userid))


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
        'password':encrypt_password(password),
    })
    return "done"


@app.route('/listing/<userid>')
@flask_login.login_required
def listing(userid):
    product_post = client[DB_NAME].carousell.find({
        'userid':ObjectId(userid)
    })
    return render_template('productpost.template.html',product_post = product_post)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return "logged out"

@app.route('/userprofile/<userid>')
def userprofile(userid):
    userid= client[DB_NAME].user.find_one()
    return render_template('userprofile.template.html',userid=userid)






# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
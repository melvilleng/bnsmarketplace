from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
client= pymongo.client(MONGO_URI)

# create the flask app and set the session
app = Flask(__name__)



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
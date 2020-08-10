from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = "book_review"

# The Home Route
# Display all the book listing
@app.route('/')
def home():
    bk = client[DB_NAME].books.find()
    return render_template('home.template.html', books=bk)

@app.route('/add/book')
def show_create_form():
    return render_template('add_book.template.html')

@app.route('/add/book', methods=['POST'])
def create_task():
    # extract information from the form
    title = request.form.get('title')
    author = request.form.get('author')
    comments = request.form.get('comments')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
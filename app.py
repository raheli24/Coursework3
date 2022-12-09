from flask import Flask, render_template, request

from api.api import api_bp
from utils import load_posts, load_post_by_pk, load_post_by_word, load_post_by_name

app = Flask(__name__)

app.register_blueprint(api_bp)


@app.route("/")
def view_main():
    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route("/post/<int:pk>")
def view_post(pk):
    post = load_post_by_pk(pk)
    return render_template('post.html', post=post)


@app.route("/search/", methods=["GET"])
def view_search():
    posts = load_post_by_word(request.args.get('search_word'))
    return render_template('search.html', posts=posts)


@app.route("/user/<user_name>")
def view_user(user_name):
    posts = load_post_by_name(user_name)
    return render_template('user-feed.html', posts=posts)


app.run(debug=True)

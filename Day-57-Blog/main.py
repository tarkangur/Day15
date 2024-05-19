import requests
from flask import Flask, render_template


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", post=all_posts)


@app.route('/blog')
def blog():
    return render_template("index.html", post=all_posts)


@app.route('/post/<num>')
def post(num):
    num = int(num) - 1
    return render_template("post.html", num=num, post=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

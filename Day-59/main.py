from flask import Flask, render_template
import requests

app = Flask("__name__")
response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact_me():
    return render_template("contact.html")


@app.route("/post/<num>")
def go_post(num):
    num = int(num) - 1
    return render_template("post.html", num=num, data=data)


if __name__ == "__main__":
    app.run(debug=True)

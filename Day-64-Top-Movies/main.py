from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests

API_KEY = os.environ["api_key"]


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///movies.db"
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class EditAdd(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for movie in all_movies:
        reverse_all_movies = all_movies[::-1]
        movie.ranking = reverse_all_movies.index(movie) + 1
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = EditAdd()
    if form.validate_on_submit():
        movie_title = form.data["title"]
        url = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(url, params={"api_key": API_KEY, "query": movie_title})
        movies = response.json()["results"]
        return render_template("select.html", movies=movies)

    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select_movie():
    movie_api_id = request.args.get("id")
    new_movie_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
    response = requests.get(new_movie_url, params={"api_key": API_KEY, "append_to_response": "title, poster_path, "
                                                                                             "release_date, overview"})
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/original{data["poster_path"]}",
        year=data["release_date"].split("-")[0]
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)

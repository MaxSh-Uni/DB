from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "key"
bootstrap = Bootstrap(app)

client = MongoClient("mongodb://localhost:27017")
db = client["movie_tracker"]

movies_col = db["movies"]
actors_col = db["actors"]
reviews_col = db["reviews"]

@app.route("/")
def index():
    sort_param = request.args.get("sort", "name")

    if sort_param == "name":
        movies = movies_col.find().sort("title", ASCENDING)
    elif sort_param == "year":
        movies = movies_col.find().sort("year", DESCENDING)
    elif sort_param == "rating":
        movies = movies_col.find().sort("rating", DESCENDING)
    else:
        movies = movies_col.find()

    return render_template("index.html", movies=movies, sort_param=sort_param)


@app.route("/movie/<movie_id>")
def movie_detail(movie_id):
    movie = movies_col.find_one({"_id": ObjectId(movie_id)})

    actors = actors_col.find({"_id": {"$in": movie.get("cast_ids", [])}})

    reviews = reviews_col.find({"movie_id": movie["_id"]})

    similar_movies = []
    if movie.get("cast_ids"):
        similar_movies = movies_col.find({
            "_id": {"$ne": movie["_id"]},
            "cast_ids": {"$in": movie["cast_ids"]}
        }).limit(10)

    return render_template("movie.html", movie=movie, actors=actors, reviews=reviews, similar_movies=similar_movies)


@app.route("/movie/<movie_id>/review", methods=["POST"])
def add_review(movie_id):
    user = request.form["user"]
    rating = int(request.form["rating"])
    comment = request.form["comment"]

    review_id = reviews_col.insert_one({
        "movie_id": ObjectId(movie_id),
        "user": user,
        "rating": rating,
        "comment": comment
    }).inserted_id

    movies_col.update_one(
        {"_id": ObjectId(movie_id)},
        {"$push": {"review_ids": review_id}}
    )

    return redirect(url_for('movie_detail', movie_id=movie_id))


@app.route("/actors")
def actor_list():
    actors = actors_col.find()
    return render_template("actors.html", actors=actors)


@app.route("/actor/<actor_id>")
def actor_detail(actor_id):
    actor = actors_col.find_one({"_id": ObjectId(actor_id)})

    movies = movies_col.find({"cast_ids": ObjectId(actor_id)})

    return render_template("actor.html", actor=actor, movies=movies)


if __name__ == "__main__":
    app.run(debug=True)

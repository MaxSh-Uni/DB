from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Для сессий
Bootstrap(app)

client = MongoClient("mongodb://localhost:27017,localhost:27018/?replicaSet=rs0")

db = client["movie_tracker"]
movies_col = db["movies"]
users_col = db["users"]

@app.route("/")
def index():
    sort = request.args.get("sort")

    sort_options = {
        "title": ("title", 1),
        "year": ("year", -1),
        "rating": ("rating", -1)
    }

    if sort in sort_options:
        field, direction = sort_options[sort]
        movies = list(movies_col.find().sort(field, direction))
    else:
        movies = list(movies_col.find())

    return render_template("index.html", movies=movies, sort=sort)

@app.route("/movie/<movie_id>")
def movie_page(movie_id):
    movie = movies_col.find_one({"_id": ObjectId(movie_id)})
    user_watchlist = []
    if "username" in session:
        user = users_col.find_one({"username": session["username"]})
        if user:
            user_watchlist = user.get("watchlist", [])

    related_movies = list(
        movies_col.find({
            "cast": {"$in": movie.get("cast", [])},
            "_id": {"$ne": movie["_id"]}
        }).limit(5)
    )
    return render_template("movie.html", movie=movie, user_watchlist=user_watchlist, related_movies=related_movies)

@app.route("/add_watchlist/<movie_id>")
def add_watchlist(movie_id):
    if "username" in session:
        users_col.update_one(
            {"username": session["username"]},
            {"$addToSet": {"watchlist": movie_id}}
        )
    return redirect(url_for("movie_page", movie_id=movie_id))

@app.route("/watchlist")
def watchlist():
    if "username" not in session:
        return redirect(url_for("login"))

    user = users_col.find_one({"username": session["username"]})
    watchlist_ids = user.get("watchlist", [])

    movies = []
    if watchlist_ids:
        movies = list(
            movies_col.find({
                "_id": {"$in": [ObjectId(mid) for mid in watchlist_ids]}
            })
        )

    return render_template("watchlist.html", movies=movies)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        if not users_col.find_one({"username": username}):
            users_col.insert_one({"username": username, "watchlist": []})
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["movie_tracker"]
movies_col = db["movies"]

movies_col.delete_many({})
movies_col.insert_many([
    {"title": "The Wolf of Wall Street", "year": 2013, "genres": ["Drama", "Crime"], "director": "Martin Scorsese", "cast": ["Leonardo DiCaprio"], "rating": 8.2},
    {"title": "Shutter Island", "year": 2010, "genres": ["Thriller", "Mystery"], "director": "Martin Scorsese", "cast": ["Leonardo DiCaprio"], "rating": 8.2},
    {"title": "Catch Me If You Can", "year": 2002, "genres": ["Drama", "Crime"], "director": "Steven Spielberg", "cast": ["Leonardo DiCaprio", "Tom Hanks"], "rating": 8.1},
    {"title": "Django Unchained", "year": 2012, "genres": ["Western", "Drama"], "director": "Quentin Tarantino", "cast": ["Jamie Foxx", "Leonardo DiCaprio"], "rating": 8.4},
    {"title": "The Revenant", "year": 2015, "genres": ["Adventure", "Drama"], "director": "Alejandro G. Inarritu", "cast": ["Leonardo DiCaprio"], "rating": 8.0},
    {"title": "Se7en", "year": 1995, "genres": ["Crime", "Thriller"], "director": "David Fincher", "cast": ["Brad Pitt", "Morgan Freeman"], "rating": 8.6},
    {"title": "Gone Girl", "year": 2014, "genres": ["Thriller", "Drama"], "director": "David Fincher", "cast": ["Ben Affleck"], "rating": 8.1},
    {"title": "The Curious Case of Benjamin Button", "year": 2008, "genres": ["Drama", "Fantasy"], "director": "David Fincher", "cast": ["Brad Pitt"], "rating": 7.8},
    {"title": "Mad Max: Fury Road", "year": 2015, "genres": ["Action", "Adventure"], "director": "George Miller", "cast": ["Tom Hardy"], "rating": 8.1},
    {"title": "John Wick", "year": 2014, "genres": ["Action", "Thriller"], "director": "Chad Stahelski", "cast": ["Keanu Reeves"], "rating": 7.9},
    {"title": "John Wick: Chapter 2", "year": 2017, "genres": ["Action", "Thriller"], "director": "Chad Stahelski", "cast": ["Keanu Reeves"], "rating": 7.4},
    {"title": "John Wick: Chapter 3", "year": 2019, "genres": ["Action", "Thriller"], "director": "Chad Stahelski", "cast": ["Keanu Reeves"], "rating": 7.4},
    {"title": "Blade Runner 2049", "year": 2017, "genres": ["Sci-Fi", "Drama"], "director": "Denis Villeneuve", "cast": ["Ryan Gosling"], "rating": 8.0},
    {"title": "Arrival", "year": 2016, "genres": ["Sci-Fi", "Drama"], "director": "Denis Villeneuve", "cast": ["Amy Adams"], "rating": 7.9},
    {"title": "Prisoners", "year": 2013, "genres": ["Thriller", "Drama"], "director": "Denis Villeneuve", "cast": ["Hugh Jackman"], "rating": 8.1},
    {"title": "La La Land", "year": 2016, "genres": ["Drama", "Music"], "director": "Damien Chazelle", "cast": ["Ryan Gosling", "Emma Stone"], "rating": 8.0},
    {"title": "Drive", "year": 2011, "genres": ["Crime", "Drama"], "director": "Nicolas Winding Refn", "cast": ["Ryan Gosling"], "rating": 7.8},
    {"title": "The Big Short", "year": 2015, "genres": ["Drama"], "director": "Adam McKay", "cast": ["Christian Bale"], "rating": 7.8},
    {"title": "No Country for Old Men", "year": 2007, "genres": ["Crime", "Drama"], "director": "Coen Brothers", "cast": ["Javier Bardem"], "rating": 8.2},
    {"title": "There Will Be Blood", "year": 2007, "genres": ["Drama"], "director": "Paul Thomas Anderson", "cast": ["Daniel Day-Lewis"], "rating": 8.2},
    {"title": "Her", "year": 2013, "genres": ["Drama", "Sci-Fi"], "director": "Spike Jonze", "cast": ["Joaquin Phoenix"], "rating": 8.0},
    {"title": "The Truman Show", "year": 1998, "genres": ["Drama"], "director": "Peter Weir", "cast": ["Jim Carrey"], "rating": 8.2},
    {"title": "Eternal Sunshine of the Spotless Mind", "year": 2004, "genres": ["Drama", "Romance"], "director": "Michel Gondry", "cast": ["Jim Carrey", "Kate Winslet"], "rating": 8.3},
    {"title": "A Beautiful Mind", "year": 2001, "genres": ["Drama"], "director": "Ron Howard", "cast": ["Russell Crowe"], "rating": 8.2},
    {"title": "Black Swan", "year": 2010, "genres": ["Drama", "Thriller"], "director": "Darren Aronofsky", "cast": ["Natalie Portman"], "rating": 8.0},
    {"title": "The Grand Budapest Hotel", "year": 2014, "genres": ["Comedy", "Drama"], "director": "Wes Anderson", "cast": ["Ralph Fiennes"], "rating": 8.1},
    {"title": "Birdman", "year": 2014, "genres": ["Drama"], "director": "Alejandro G. Inarritu", "cast": ["Michael Keaton"], "rating": 7.7},
    {"title": "The Hateful Eight", "year": 2015, "genres": ["Western", "Drama"], "director": "Quentin Tarantino", "cast": ["Samuel L. Jackson"], "rating": 7.8},
    {"title": "Once Upon a Time in Hollywood", "year": 2019, "genres": ["Drama", "Comedy"], "director": "Quentin Tarantino", "cast": ["Leonardo DiCaprio", "Brad Pitt"], "rating": 7.6},
    {"title": "The Silence of the Lambs", "year": 1991, "genres": ["Thriller", "Crime"], "director": "Jonathan Demme", "cast": ["Anthony Hopkins"], "rating": 8.6},
    {"title": "Heat", "year": 1995, "genres": ["Crime", "Drama"], "director": "Michael Mann", "cast": ["Al Pacino", "Robert De Niro"], "rating": 8.2},
    {"title": "Scarface", "year": 1983, "genres": ["Crime", "Drama"], "director": "Brian De Palma", "cast": ["Al Pacino"], "rating": 8.3},
    {"title": "Casino", "year": 1995, "genres": ["Crime", "Drama"], "director": "Martin Scorsese", "cast": ["Robert De Niro"], "rating": 8.2},
    {"title": "Donnie Darko", "year": 2001, "genres": ["Drama", "Sci-Fi"], "director": "Richard Kelly", "cast": ["Jake Gyllenhaal"], "rating": 8.0},
    {"title": "Nightcrawler", "year": 2014, "genres": ["Thriller", "Drama"], "director": "Dan Gilroy", "cast": ["Jake Gyllenhaal"], "rating": 7.9},
    {"title": "The Prestige", "year": 2006, "genres": ["Drama", "Mystery"], "director": "Christopher Nolan", "cast": ["Christian Bale", "Hugh Jackman"], "rating": 8.5},
    {"title": "Memento", "year": 2000, "genres": ["Thriller", "Mystery"], "director": "Christopher Nolan", "cast": ["Guy Pearce"], "rating": 8.4},
    {"title": "Insomnia", "year": 2002, "genres": ["Thriller"], "director": "Christopher Nolan", "cast": ["Al Pacino"], "rating": 7.2},
    {"title": "Batman Begins", "year": 2005, "genres": ["Action", "Drama"], "director": "Christopher Nolan", "cast": ["Christian Bale"], "rating": 8.2},
    {"title": "The Departed", "year": 2006, "genres": ["Crime", "Drama"], "director": "Martin Scorsese", "cast": ["Leonardo DiCaprio"], "rating": 8.5},
    {"title": "Logan", "year": 2017, "genres": ["Action", "Drama"], "director": "James Mangold", "cast": ["Hugh Jackman"], "rating": 8.1},
    {"title": "The Imitation Game", "year": 2014, "genres": ["Drama"], "director": "Morten Tyldum", "cast": ["Benedict Cumberbatch"], "rating": 8.0},
    {"title": "12 Years a Slave", "year": 2013, "genres": ["Drama"], "director": "Steve McQueen", "cast": ["Chiwetel Ejiofor"], "rating": 8.1},
    {"title": "Moonlight", "year": 2016, "genres": ["Drama"], "director": "Barry Jenkins", "cast": ["Mahershala Ali"], "rating": 7.4},
    {"title": "The Green Mile", "year": 1999, "genres": ["Drama"], "director": "Frank Darabont", "cast": ["Tom Hanks"], "rating": 8.6}
])

print("Movies inserted")

actors_col = db["actors"]

actors_col.delete_many({})
actors_col.insert_many([
    {"name": "Leonardo DiCaprio", "birth_year": 1974, "nationality": "USA"},
    {"name": "Brad Pitt", "birth_year": 1963, "nationality": "USA"},
    {"name": "Tom Hanks", "birth_year": 1956, "nationality": "USA"},
    {"name": "Jamie Foxx", "birth_year": 1967, "nationality": "USA"},
    {"name": "Keanu Reeves", "birth_year": 1964, "nationality": "Canada"},
    {"name": "Ryan Gosling", "birth_year": 1980, "nationality": "Canada"},
    {"name": "Emma Stone", "birth_year": 1988, "nationality": "USA"},
    {"name": "Hugh Jackman", "birth_year": 1968, "nationality": "Australia"},
    {"name": "Christian Bale", "birth_year": 1974, "nationality": "UK"},
    {"name": "Al Pacino", "birth_year": 1940, "nationality": "USA"},
    {"name": "Robert De Niro", "birth_year": 1943, "nationality": "USA"},
    {"name": "Jake Gyllenhaal", "birth_year": 1980, "nationality": "USA"},
    {"name": "Michael Keaton", "birth_year": 1951, "nationality": "USA"},
    {"name": "Natalie Portman", "birth_year": 1981, "nationality": "Israel/USA"},
    {"name": "Benedict Cumberbatch", "birth_year": 1976, "nationality": "UK"},
    {"name": "Chiwetel Ejiofor", "birth_year": 1977, "nationality": "UK"},
    {"name": "Mahershala Ali", "birth_year": 1974, "nationality": "USA"}
])

print("Actors inserted")

# ---------- Reviews ----------
reviews_col = db["reviews"]

reviews_col.delete_many({})
reviews_col.insert_many([
    {"movie_title": "The Wolf of Wall Street", "user": "user1", "rating": 9, "comment": "Amazing performance by DiCaprio!"},
    {"movie_title": "Shutter Island", "user": "user2", "rating": 8, "comment": "Great thriller with unexpected twists."},
    {"movie_title": "Catch Me If You Can", "user": "user3", "rating": 8, "comment": "Fun and engaging story."},
    {"movie_title": "Django Unchained", "user": "user4", "rating": 9, "comment": "Excellent Tarantino film."},
    {"movie_title": "The Revenant", "user": "user5", "rating": 7, "comment": "Brutal but visually stunning."},
    {"movie_title": "Se7en", "user": "user6", "rating": 10, "comment": "Classic thriller, very intense."},
    {"movie_title": "Mad Max: Fury Road", "user": "user7", "rating": 8, "comment": "Non-stop action, visually amazing."},
    {"movie_title": "John Wick", "user": "user8", "rating": 7, "comment": "Great action choreography."},
    {"movie_title": "Blade Runner 2049", "user": "user9", "rating": 9, "comment": "Beautiful cinematography and story."},
    {"movie_title": "La La Land", "user": "user10", "rating": 8, "comment": "Lovely musical, fantastic chemistry."}
])

print("Reviews inserted")


actors = list(actors_col.find())
actor_name_to_id = {actor['name']: actor['_id'] for actor in actors}

for movie in movies_col.find():
    cast_ids = [actor_name_to_id[name] for name in movie['cast'] if name in actor_name_to_id]
    movies_col.update_one(
        {'_id': movie['_id']},
        {'$set': {'cast_ids': cast_ids}}
    )

print("Movies linked with actors")

movies = list(movies_col.find())
title_to_id = {movie['title']: movie['_id'] for movie in movies}

for review in reviews_col.find():
    movie_title = review['movie_title']
    if movie_title in title_to_id:
        movies_col.update_one(
            {'_id': title_to_id[movie_title]},
            {'$push': {'review_ids': review['_id']}}
        )
        reviews_col.update_one(
            {'_id': review['_id']},
            {'$set': {'movie_id': title_to_id[movie_title]}}
        )

print("Reviews linked with movies")


print("Database initialized")
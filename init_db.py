from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017,localhost:27018/?replicaSet=rs0")
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

# movies_col.insert_many(movies)

print("Database initialized")
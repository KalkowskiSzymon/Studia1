import csv
from flask_restful import Resource


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

    def __dict__(self):
        return {
            "movieId": self.movieId,
            "title": self.title,
            "genres": self.genres,
        }


class Movies(Resource):
    def get(self):
        movies = []
        with open("movies.csv", mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movie = Movie(
                    movieId=row["movieId"],
                    title=row["title"],
                    genres=row["genres"],
                )
                movies.append(movie.__dict__())
        return movies

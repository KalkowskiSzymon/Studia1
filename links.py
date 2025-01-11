import csv
from flask_restful import Resource


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

    def __dict__(self):
        return {
            "movieId": self.movieId,
            "imdbId": self.imdbId,
            "tmdbId": self.tmdbId,
        }


class Links(Resource):
    def get(self):
        links = []
        with open("links.csv", mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                link = Link(
                    movieId=row["movieId"],
                    imdbId=row["imdbId"],
                    tmdbId=row["tmdbId"],
                )
                links.append(link.__dict__())
        return links

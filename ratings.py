import csv
from flask_restful import Resource


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "rating": self.rating,
            "timestamp": self.timestamp,
        }


class Ratings(Resource):
    def get(self):
        ratings = []
        with open("ratings.csv", mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                rating = Rating(
                    userId=row["userId"],
                    movieId=row["movieId"],
                    rating=row["rating"],
                    timestamp=row["timestamp"],
                )
                ratings.append(rating.__dict__())
        return ratings

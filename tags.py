import csv
from flask_restful import Resource


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

    def __dict__(self):
        return {
            "userId": self.userId,
            "movieId": self.movieId,
            "tag": self.tag,
            "timestamp": self.timestamp,
        }


class Tags(Resource):
    def get(self):
        tags = []
        with open("tags.csv", mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                tag = Tag(
                    userId=row["userId"],
                    movieId=row["movieId"],
                    tag=row["tag"],
                    timestamp=row["timestamp"],
                )
                tags.append(tag.__dict__())
        return tags

from flask import Flask
from flask_restful import Api
from movies import Movies
from helloworld import HelloWorld
from links import Links
from tags import Tags
from ratings import Ratings

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, "/")
api.add_resource(Movies, "/movies")
api.add_resource(Links, "/links")
api.add_resource(Tags, "/tags")
api.add_resource(Ratings, "/ratings")

if __name__ == "__main__":
    app.run(debug=True)

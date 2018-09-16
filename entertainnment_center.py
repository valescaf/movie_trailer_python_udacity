# Import Media and Fresh Tomatoes
import media
import fresh_tomatoes
# Import JSON
import json
# Import Flask
from flask import Flask
from flask import jsonify

# Make the movie instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to live",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A Marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
school_of_rock = media.Movie("Schoof of Rock",
                             "A story of a ex-Rock start that became a teacher at a school of music",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                          "A mouse that helps a boy to cook",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "http://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "A writer travel to the past in Paris",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                           "A girl fight to save the people from the governance",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "http://www.youtube.com/watch?v=PbA63a7H0bo")

# Creating a list of Objects for passing the movies object to
# The Fresh Tomatoes File to display
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# Create a string by list
movies_string = json.dumps(movies, default=lambda x: x.__dict__)

# Calling the funtion present in fresh_tomatoes to display the
# movie list and show trailer in Webbrowser
fresh_tomatoes.open_movies_page(movies)

# Create API
app = Flask(__name__)


@app.route("/movies")
def Movies_json():
    return (movies_string)

if __name__ == "__main__":
    app.run()

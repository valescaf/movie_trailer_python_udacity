import webbrowser


class Movie():
        """This class provide a way to store movie related information"""
        # Constructor Initializing value for each object
        # title : Movie name
        # storyline : Gist of movie
        # poster_image_url : Movie Poster
        # trailer_youtube   : Youtube Trailer
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

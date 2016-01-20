import webbrowser


class Movie():
    def __init__(
        self,
        movie_title,
        movie_storyline,
        movie_actors,
        poster_image,
        trailer_youtube,
        trailer_vimeo,
     ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.actors = movie_actors
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.criticism = trailer_vimeo

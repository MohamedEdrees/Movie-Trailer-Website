class Movie():
    """ This class store movie related information

    Attributes:
        title: The title of the movie
        poster_image_url: The URL address of a poster of the movie
        trailer_youtube_url: A link to a YouTube shows the trailer of the movie
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

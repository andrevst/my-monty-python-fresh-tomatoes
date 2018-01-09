import webbrowser


class Movie():
    """ This class create a movie and shows some of it`s information.

        Arguments:
            title: Movie name
            year: The release year of the movie
            sinopse: A brief description of the movie
            poster_img_url: Wikipedia image poster link
            trailer_youtube_id: Youtube link for the trailer
    """
    def __init__(self, title, year,
                 sinopse, poster_img_url, trailer_youtube_url):
        self.title = title  # Movie name
        self.year = year  # Movie premiere year
        self.sinopse = sinopse  # A brief description of it
        self.poster_img_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url


# open youtube link and show the trailer
def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

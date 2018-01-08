import webbrowser

class Movie():
    """ This class create a movie and shows some of it`s information like YEAR, SINOPSE and TRAILER. """

    def __init__ (self,title,year,sinopse,poster_img_url,trailer_youtube_url):
        self.title = title  # Movie name
        self.year = year  # Movie premiere year
        self.sinopse = sinopse  # A brief description of it
        self.poster_img_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

# open youtube link for the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

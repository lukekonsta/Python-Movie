import webbrowser

class Movie():
    """This class is responsible for providing movie info"""
    valid_ratings = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, movie_poster, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer)
        

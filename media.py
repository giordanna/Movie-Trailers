# -*- coding: utf-8 -*-
import webbrowser

class Movie():
    """ A class for dealing with movie informations """
    
    #VALID_RATINGS = ["G" ,"PG", "PG-13", "R", "NC-17"]
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
# -*- coding: utf-8 -*-
import webbrowser


class Movie():
    """ Classe que lida com informações relacionadas a filmes """

    def __init__(self, movie_title, movie_storyline, movie_poster_image,
                 movie_youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

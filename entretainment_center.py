# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
import time
import tmdbsimple as tmdb

tmdb.API_KEY = 'CHAVE_API'

# faz busca dos filmes que estão em cartaz nos cinemas
movies = tmdb.Movies()
response = movies.now_playing()
movies_array = []

for m in movies.results:

    print("Gerando entrada de filme para '" + m['title'] + "' em "
          + time.ctime())

    # constrói o link para o poster do filme
    poster_url = 'https://image.tmdb.org/t/p/original' + m['poster_path']
    trailer_url = ""

    # busca entre os videos relacionados do filme o que for do tipo "Trailer"
    # e constrói o link para o video do youtube
    movie = tmdb.Movies(m['id'])
    response = movie.videos()

    for v in movie.results:
        if v['type'] == 'Trailer' and v['site'] == 'YouTube':
            trailer_url = 'https://www.youtube.com/watch?v=' + v['key']
            break

    # cria o objeto do filme e adiciona na lista
    movies_array.append(
            media.Movie(
                    m['title'],
                    m['overview'],
                    poster_url,
                    trailer_url
                    )
            )

print("\nGeração da página concluída em " + time.ctime() + "!" )

# cria a página com a lista de filmes como entrada
fresh_tomatoes.open_movies_page(movies_array)

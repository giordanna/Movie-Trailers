# -*- coding: utf-8 -*-

import media, fresh_tomatoes

mad_max = media.Movie("Mad Max: Fury Road",
                       "Max acredita que a melhor forma de sobreviver é não depender de mais ninguém além de si próprio",
                       "https://upload.wikimedia.org/wikipedia/pt/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
                       "https://www.youtube.com/watch?v=hEJnMQG9ev8")

pantera_negra = media.Movie("Pantera Negra",
                       "Depois dos eventos de Capitão América: Guerra Civil, após a morte de T'Chaka, seu filho T'Challa retorna a Wakanda para assumir o trono",
                       "https://upload.wikimedia.org/wikipedia/pt/9/90/Pantera_Negra_%28poster%29.jpg",
                       "https://www.youtube.com/watch?v=xjDjIWPwcPU")

deadpool_2 = media.Movie("Deadpool 2",
                       "Depois de trabalhar com sucesso como o mercenário Deadpool por dois anos, Wade Wilson não consegue matar um de seus alvos em seu aniversário com sua namorada Vanessa",
                       "https://upload.wikimedia.org/wikipedia/pt/4/46/Deadpool_2.jpg",
                       "https://www.youtube.com/watch?v=1P9OzWX6nzE")

logan = media.Movie("Logan",
                       "Em 2029, os mutantes estão à beira da extinção, com nenhum novo mutante tendo nascido em 25 anos",
                       "https://upload.wikimedia.org/wikipedia/pt/2/2d/Filme_Logan_2017.jpg",
                       "https://www.youtube.com/watch?v=KPND6SgkN7Q")

ghost_shell = media.Movie("Ghost in the Shell",
                       "Num futuro próximo, a maior parte dos seres humanos possui implantes cibernéticos, aprimorando várias características como visão, força e inteligência",
                       "https://upload.wikimedia.org/wikipedia/pt/d/d1/Ghost_in_the_Shell.jpg",
                       "https://www.youtube.com/watch?v=G4VmJcZR0Yg")

jogo_imitacao = media.Movie("O Jogo da Imitação",
                       "Em 1951, dois policiais investigam o matemático Alan Turing após o que aparenta ser uma invasão de sua casa. Suspeitando de seu comportamento e falta de registros de guerra, decidem interrogar Turing com medo que ele seja um espião",
                       "https://upload.wikimedia.org/wikipedia/pt/1/1a/O_Jogo_da_Imita%C3%A7%C3%A3o.jpg",
                       "https://www.youtube.com/watch?v=YIkKbMcJL_4")

movies = [deadpool_2, ghost_shell, jogo_imitacao, logan, mad_max, pantera_negra]
fresh_tomatoes.open_movies_page(movies)
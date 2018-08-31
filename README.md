# Site de trailer de filmes
Primeiro projeto do curso de Desenvolvedor Full Stack da Audacity.
Este projeto permite gerar um site estático de trailer de filmes usando python.

### Como instalar
- Clone ou baixe este repositório;
- Execute o arquivo entretainment_center.py no seu editor de preferência ou através do terminal utilizando:
```sh
python entretainment_center.py
```
- Aguarde até que o arquivo fresh_tomatoes.html seja gerado. Ele será aberto automaticamente em seu navegador.
**OBS:** certifique-se de que possui o python instalado.

### Como modificar os filmes
- Abra o arquivo entretainment_center.py no seu editor de preferência e adicione:
```python
nome_filme = media.Movie("Nome do filme",
                         "História do filme",
                         "Link do poster do filme",
                         "Link do trailer no youtube do filme")
```
- Você pode apagar os outros que estão como amostra caso desejar;
- Por fim, não esqueça de adicionar a lista de filmes para passar como argumento para o gerador do site:
```python
movies = [..., nome_filme]
fresh_tomatoes.open_movies_page(movies)
```

### Todos
 - Refazer o layout do site do zero
 - Utilizar uma API para listar filmes
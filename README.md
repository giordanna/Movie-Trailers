# Site de trailer de filmes
Primeiro projeto do curso de Desenvolvedor Full Stack da Audacity.
Este projeto permite gerar um site estático de trailer de filmes usando python.

[Veja o site no ar](https://giordanna.github.io/Movie-Trailers/fresh_tomatoes.html)

### Como instalar
- Clone ou baixe este repositório;
- Certifique-se de que possui a API de filmes tmdbsimple instalada, execute em seu terminal:
```sh
pip install tmdbsimple
```
- Execute o arquivo entretainment_center.py no seu editor de preferência ou através do terminal utilizando:
```sh
python entretainment_center.py
```
- Aguarde até que o arquivo fresh_tomatoes.html seja gerado. Ele será aberto automaticamente em seu navegador.
**OBS:** certifique-se de que possui o python instalado.

### Chave da API
Você vai precisar de uma chave da API do The Movie Database. Para obter a chave:

1) [Registre-se](https://www.themoviedb.org/account/signup) no site;
2) [Faça login](https://www.themoviedb.org/login) na sua conta;
3) Selecione a seção API no canto esquerdo em "Configurações" da sua conta;
4) Clique no link para gerar a chave e siga as instruções;
5) Ao obter a chave, vá em entretainment_center.py e substitua CHAVE_API por sua chave:

```python
tmdb.API_KEY = 'CHAVE_API'
```

### Como modificar os filmes
- Abra o arquivo entretainment_center.py no seu editor de preferência e modifique:
```python
response = movies.now_playing()
```
- Verifique as demais funções disponíveis no código-fonte do [tmdbsimple](https://github.com/celiao/tmdbsimple).

### TODOs
 - Refazer o layout do site do zero
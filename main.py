from fastapi import FastAPI
import pandas as pd

from sklearn.metrics.pairwise        import cosine_similarity
from sklearn.metrics.pairwise        import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


app=FastAPI(debug=True)

df = pd.read_csv('df_last.csv')


@app.get('/')
def message():
    return 'proyecto integrador'

@app.get('/PlayTimeGenre/')
def PlayTimeGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    max_playtime_year = year_playtime_df.loc[year_playtime_df['playtime_forever'].idxmax(), 'year']
    return {"Género": genre, "Año de lanzamiento con más horas jugadas para Género :": int(max_playtime_year)}

@app.get('/UserForGenre/')
def UserForGenre(genre: str) -> dict:
    genre = genre.capitalize()
    genre_df = df[df[genre] == 1]
    max_playtime_user = genre_df.loc[genre_df['playtime_forever'].idxmax(), 'user_id']
    year_playtime_df = genre_df.groupby('year')['playtime_forever'].sum().reset_index()
    playtime_list = year_playtime_df.to_dict(orient='records')
    result = {
        "Usuario con más horas jugadas para Género " + genre: max_playtime_user,
        "Horas jugadas": playtime_list}
    return result

@app.get('/UserRecommend/')
def message():
    return 'abc'


@app.get('/UserNotRecommend/')
def message():
    return 'abcd'
 



muestra = df.head(4000)
tfidf = TfidfVectorizer(stop_words='english')
muestra=muestra.fillna("")

tdfid_matrix = tfidf.fit_transform(muestra['review'])
cosine_similarity = linear_kernel( tdfid_matrix, tdfid_matrix)



@app.get('/recomendacion_juego/{id_juego}')
def recomendacion_juego(id_juego: int):
    if id_juego not in muestra['id'].values:
        return {'mensaje': 'No existe el id del juego.'}
    titulo = muestra.loc[muestra['id'] == id_juego, 'title'].iloc[0]
    idx = muestra[muestra['title'] == titulo].index[0]
    sim_cosine = list(enumerate(cosine_similarity[idx]))
    sim_scores = sorted(sim_cosine, key=lambda x: x[1], reverse=True)
    sim_ind = [i for i, _ in sim_scores[1:6]]
    sim_juegos = muestra['title'].iloc[sim_ind].values.tolist()
    return {'juegos recomendados': list(sim_juegos)}
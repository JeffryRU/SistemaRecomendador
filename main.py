from db.mongodb import connect_to_mongodb, insert_movies, insert_movie_details
from api.themoviedb import fetch_movies, fetch_movie_details
from processing.data_cleaning import clean_movies
from processing.feature_engineering import prepare_features, normalize_data
from recomendation.similarity_logic import recommend_movies
def main():
    # Conectar a MongoDB
    db = connect_to_mongodb()
    movies_collection = db['movies']
    movie_details_collection = db['movie_details']
    # Extraer y cargar películas desde la API de TMDb
    for page in range(1, 6):
        movies = fetch_movies(page)
        insert_movies(movies_collection, movies)
    # Extraer detalles de las películas
    for movie in movies_collection.find():
        movie_id = movie['id']
        details = fetch_movie_details(movie_id)
        insert_movie_details(movie_details_collection, details)
    # Limpieza y transformación de datos
    clean_movies_data = clean_movies(movie_details_collection)
    # Preparar características
    features = prepare_features(clean_movies_data)
    normalized_features = normalize_data(features)
    # Recomendaciones
    movie_title = "The Crow"
    recommendations = recommend_movies(movie_title, normalized_features, top_n=5)
    print(f"Recomendaciones para '{movie_title}':", recommendations)
if __name__ == "__main__":
    main()
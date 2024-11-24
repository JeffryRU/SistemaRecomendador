from pymongo import MongoClient
from config import TMDB_API_KEY, TMDB_BASE_URL
def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    print("Conexión establecida con MongoDB.")
    return client['RecomendationSystem_db']
def insert_movies(collection, movies):
    for movie in movies:
        if not collection.find_one({"id": movie["id"]}):
            collection.insert_one(movie)
            print(f"Película '{movie['title']}' almacenada en MongoDB.")
def insert_movie_details(collection, details):
    if not collection.find_one({"id": details["id"]}):
        collection.insert_one(details)
        print(f"Detalles de la película ID {details['id']} almacenados en MongoDB.")
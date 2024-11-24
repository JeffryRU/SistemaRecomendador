import requests
from config import TMDB_API_KEY, TMDB_BASE_URL
def fetch_movies(page):
    url = f"{TMDB_BASE_URL}/popular?language=en-US&page={page}"
    headers = {"Authorization": f"Bearer {TMDB_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Página {page}: {len(data.get('results', []))} películas encontradas.")  # Para depurar
        return data.get("results", [])
    else:
        print(f"Error al obtener películas en la página {page}: {response.status_code} {response.text}")
        return []
def fetch_movie_details(movie_id):
    url = f"{TMDB_BASE_URL}/{movie_id}?language=en-US"
    headers = {"Authorization": f"Bearer {TMDB_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Detalles de película para ID {movie_id} obtenidos correctamente.")  # Para depurar
        return data
    else:
        print(f"Error al obtener detalles de película para ID {movie_id}: {response.status_code} {response.text}")
        return {}
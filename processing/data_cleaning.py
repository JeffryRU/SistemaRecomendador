import pandas as pd
def clean_movies(collection):
    movies = list(collection.find())
    df = pd.DataFrame(movies)
    df['genres'] = df['genres'].apply(lambda x: [g['name'] for g in x] if isinstance(x, list) else [])
    return df
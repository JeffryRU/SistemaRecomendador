from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
def recommend_movies(movie_title, features, top_n=5):
    if movie_title not in features.index:
        return f"La película '{movie_title}' no está en el sistema."
    similarity_matrix = cosine_similarity(features)
    similarity_df = pd.DataFrame(similarity_matrix, index=features.index, columns=features.index)
    similar_movies = similarity_df[movie_title].sort_values(ascending=False)[1:top_n+1]
    return similar_movies.index.tolist()
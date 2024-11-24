from sklearn.preprocessing import MinMaxScaler, MultiLabelBinarizer
import pandas as pd
def prepare_features(df):
    mlb = MultiLabelBinarizer()
    genres_encoded = mlb.fit_transform(df['genres'])
    genres_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)
    features = df[['vote_average', 'vote_count']].join(genres_df)
    return features
def normalize_data(features):
    scaler = MinMaxScaler()
    normalized = scaler.fit_transform(features)
    return pd.DataFrame(normalized, columns=features.columns)
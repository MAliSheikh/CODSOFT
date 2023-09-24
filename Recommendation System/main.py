import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import linear_kernel


def get_data(csv_file):
    data = pd.read_csv(csv_file)
    return data


db_movies = get_data('tmdb_5000_movies.csv')

def calculate_cosine_similarity(df, text_column):
    tfidf = TfidfVectorizer(stop_words='english')
    
    df[text_column] = df[text_column].fillna('')
    
    tfidf_matrix = tfidf.fit_transform(df[text_column])
    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['original_title']).drop_duplicates()
    
    return cosine_sim, indices

cosine_sim, indices = calculate_cosine_similarity(db_movies, 'overview')

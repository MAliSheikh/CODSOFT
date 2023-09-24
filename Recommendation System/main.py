import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import linear_kernel


def get_data(csv_file):
    data = pd.read_csv(csv_file)
    return data



def calculate_cosine_similarity(df, text_column):
    tfidf = TfidfVectorizer(stop_words='english')
    
    df[text_column] = df[text_column].fillna('')
    
    tfidf_matrix = tfidf.fit_transform(df[text_column])
    
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['original_title']).drop_duplicates()
    
    return cosine_sim, indices

def get_recommendation(title, cosine_sim, indices):
    idx = indices[title]
    sim_scores = enumerate(cosine_sim[idx])

    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)   

    sim_scores = sim_scores[1:11]
    
    sim_index = [i[0] for i in sim_scores]
    
    print(db_movies['original_title'].iloc[sim_index])


db_movies = get_data('tmdb_5000_movies.csv')
cosine_similarity_matrix, movie_indices = calculate_cosine_similarity(db_movies, 'overview')

movie_name = input("Enter the movie name: ")
recommendations = get_recommendation(movie_name, cosine_similarity_matrix, movie_indices)
print(recommendations)
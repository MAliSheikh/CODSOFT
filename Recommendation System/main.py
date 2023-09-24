import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import linear_kernel


def get_data(csv_file):
    data = pd.read_csv(csv_file)

    list_data = []
    for col in data.columns:
        list_data.append(data[col])
    
    return list_data

print(get_data('tmdb_5000_credits.csv'))

db_movies = pd.read_csv('tmdb_5000_movies.csv')

print(db_movies.head())


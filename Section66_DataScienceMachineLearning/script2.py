# Content Based Filtering 
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer # Usefull for vectorizing the info of the 'overview' column.

# The excel file data is separated by semicolumns
movies = pd.read_csv('movies_small.csv', sep=";")
print(movies)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Searchs for null values in the Overview List
movies["overview"] = movies['overview'].fillna("")
print(movies["overview"])

tfidf_matrix = tfidf.fit_transform(movies["overview"])

tfidf_matrix = tfidf.fit_transform(movies["overview"])
print(pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out()))

# Similarity Matrix
from sklearn.metrics.pairwise import linear_kernel
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
print(cosine_sim)
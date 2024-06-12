# Data Science and Machine Learning

Welcome to the "Data Science and Machine Learning" category, where you'll embark on an exciting journey into the world of data science and machine learning using Python. In this category, you'll dive deep into the field of data science and explore techniques to extract insights from data, make predictions, and build intelligent systems.

We will undertake an exciting project in this category which is building a movie recommendation system. By applying various data science and machine learning techniques, you'll develop a system that suggests personalized movie recommendations based on user preferences. 

# Building a Movie recommendation System in Python

Three Types of Recommendation Systems:
1. Popularity Based
2. Collaborative
3. Content Based filtering

# DEEP NOTE - Use to use Google Colab
Go to https://deepnote.com/workspace/ardit-sulce-b001752f-770f-4dd6-9baf-e93ddb67c21e/project/Movie-Recommendation-System-48f880f8-2f58-41e7-b0c8-ce2863059d0d/notebook/Notebook%203-c52a48c64230407c9203ce7e5b908a1d
which is similar to Google Colab.

Calculate a weighted rating
The formula is as follows: WR = (v/ (v+m)) * R + (m/(v+m)) * C

v = Number of votes for a movie(movies.vote_count)
m = Minimum number of votes required to be consider as a popular Movie
R = Average rating of a movie(movies.vote_average)
C = Average rating accross all movies
NOTE: We need to calculate m and C because those 2 values are not part of above .csv files.

# Install scipy for interacting with. We might need to use it to vectorize the text
pip install scikit-learn


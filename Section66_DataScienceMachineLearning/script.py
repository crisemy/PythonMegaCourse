'''
Calculate a weighted rating
The formula is as follows: WR = (v/ (v+m)) * R + (m/(v+m)) * C

v = Number of votes for a movie(movies.vote_count)
m = Minimum number of votes required to be consider as a popular Movie
R = Average rating of a movie(movies.vote_average)
C = Average rating accross all movies
NOTE: We need to calculate m and C because those 2 values are not part of above .csv files.
'''

import pandas

movies = pandas.read_csv('movies.csv')
ratings = pandas.read_csv('ratings.csv')
credits = pandas.read_csv('credits.csv')

# Calculation m. Note: Quantile could be modified according to your needs.
m = movies["vote_count"].quantile(0.9)
print(m)

# Calculation the average rating accross all movies
C = movies["vote_average"].mean()
print(C)

# Let's calculate the Weighted Rating (WR) which is THE formula
# The formula is: WR = (v/ (v+m)) * R + (m/(v+m)) * C

# Calculate that the m/(m+v) is not divided by Zero.
movies_filtered = movies.copy().loc[movies["vote_count"] >= m]
movies_filtered.shape
# Creating the function to perform the Formula. Sending those variable values that were calculated(m and C)
def weighted_rating(x, m=m, C=C): 
  v = x["vote_count"]
  R = x["vote_average"]
  return (v/(v+m) * R) + (m/(m+v) * C)

# To add those values as part of a new column at the end of the .csv file
movies_filtered["weighted_rating"] = movies_filtered.apply(weighted_rating, axis=1)
print(movies_filtered)

# Showing off the List of 10 elements with just the Title and the Weighted_rating column
print(movies_filtered.sort_values("weighted_rating", ascending=False)[["title", "weighted_rating"]].head(10))
print()
# Creates a dictionary that would be useful for gathering the info with an API code, a Json file for a Website from some sort
print(f"Info gattered into a dictonary")
print(movies_filtered.sort_values("weighted_rating", ascending=False)[["title", "weighted_rating"]].head(10).to_dict())


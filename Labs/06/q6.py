'''
Write a Pandas program to find out the alcohol consumption details in the year '1987' or '1989' from the world alcohol consumption dataset.
'''

#We are working on the movies data set and not on alcohol data set.. 
#So we will print the details of the movies released in the years from 1987 and 1989

import pandas as pd

df = pd.read_csv("C:\\Users\\k230006\\Desktop\\lab6\\movie_metadata.csv")
result = df[(df["title_year"] == 1987) | (df["title_year"] == 1989)]
print(result[["movie_title", "title_year"]])

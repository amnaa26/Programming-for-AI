#We are working on the movies data set andnot on alcohol data set.. 
#So we will print the details of the movies realesd in the years from 1987 and 1989

import pandas as pd

df = pd.read_csv("C:\\Users\\k230006\\Desktop\\lab6\\movie_metadata.csv")
result = df[(df["title_year"] == 1987) | (df["title_year"] == 1989)]
print(result[["movie_title", "title_year"]])
import pandas as pd

df = pd.read_csv("C:\\Users\\k230006\\Downloads\\Analyzing-the-IMDB-Movie-Dataset-master\\Analyzing-the-IMDB-Movie-Dataset-master\\movie_metadata.csv")
df = df.dropna()
result = df.sort_values(by = "title_year", ascending = False)
result.to_csv("C:\\Users\\k230006\\Downloads\\movie_sorted_metadata.csv", index = False)
print(result)
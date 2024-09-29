import pandas as pd

data = pd.read_csv("alcohol-data-text.csv")
print("Shape of the dataset:", data.shape)
data.info()
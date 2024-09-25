import pandas as pd

student = {
    "Name" : ['Laiba', 'Amna', 'Alisha', 'Layyana'],
    "Last name": ['Zia-ul-Haq', 'NaN', 'Zaidi', 'Junaid'],
    "IDs" : ['23k-0006', '23k-0066', '23k-0025', '23k-0056'],
    "CGPA" : [1.6, 4.0, 3.4, 3.34]

}

df = pd.DataFrame(data = student)
myindex = pd.Index(range(1, 1+len(df)))
df.index = myindex
print(df)
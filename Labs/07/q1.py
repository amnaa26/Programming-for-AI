# Amna (23k-0066)
# Date: 2/oct/2024

#Trying filtering in pandas. We do it to analyze data of a particular row

'''ca = df[df["cp"] == 2 ]
print(ca)
print("\nMean of cp: ")
print(ca.mean())


Filtering through groupby:
1.single group single column
2.single group multiple column
3.multiple group single column 
4.multiple group multiple colummn

#single group
cp_group = df.groupby("cp")

#single group single column anaylsis
print(cp_group['age'].mean())

#single group multiple column
print(cp_group[['age', 'ca']].mean())


#multiple group
cp_group2 = df.groupby(['cp', 'ca'])

#multiple group single column
print(cp_group2['age'].mean())

#multiple group multiple column
print(cp_group2[['age', 'ca']].mean())'''

import pandas as pd

df = pd.read_csv("dataset.csv")
df.rename(columns= {'sex': 'gender'}, inplace = True)
df['gender'] = df['gender'].replace({0: 'F', 1: 'M'})
print(df)

male_records = df[df['gender'] == 'M']
female_records = df[df['gender'] == 'F']
print("Male records:", male_records)
print("Female records:", female_records)

print("\nMale records: ")
print(male_records.describe())
print("\nFemale records: ")
print(female_records.describe())

#single g
df1 = df.groupby('gender')
#single c
print(df1['chol'].max(), end = '\n\n')
print(df1['chol'].median(), end = '\n\n')
print(df1['chol'].mean(), end = '\n\n')
#multi c
print(df1[['restecg', 'oldpeak', 'chol']].max(), end = '\n\n')
print(df1[['restecg', 'oldpeak', 'chol']].median(), end = '\n\n')
print(df1[['restecg', 'oldpeak', 'chol']].mean(), end = '\n\n')


'''
Three methods for merging:
concate --> result = pd.concat([d1, d2], axis = 1) where d1 and d2 are dataframes; axis = 1 means it will merge with column (axis = 1 means column and axis = 0 means row)
            axis = 1 means combine horizontally and axis = 1 means combine vertically
            if two same columns exists in both dataframes then combine vertically i.e axis = 0
merge --> merged_data = data1.merge(data2, how = 'inner', on = 'age') it will merge the age column of both data1 and data2 inner = intersection
          merged_data = data1.merge(data2, how = 'outer', on = 'age') outer = union;       if on = 'name' then if diff age for same names exists then it will add a new column as age_x and age_y where diff ages of same names will be stored
          how have other parameters as well such as right and left
join

Cleaning dataset:
0 is not a missing value!!!!! NaN is a missing valuee!!!!
df.dropna(inplace = True) --> drop the rows where a value is missing
df.isnull().sum() --> will give a count of missing values existing in each column
df.fillna(66, inplace = True) --> fill the same value entered as parameter in all the missing values
df.fillna(df.mean(), inplace = True) --> mean() for numeric values
what is backfill() method?
df.fillna(df.mode(), inplace = True) --> mode() will change string values
how to change categorial values?
'''
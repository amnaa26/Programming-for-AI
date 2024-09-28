#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

import re

text = """ The event will take place on 12/09/2024 and will end by 2024-09-12. Another important date is Sep 12, 2024.
        The deadlines are 09/08/2024 and August 15, 2022. Meetings will be held on 2024-12-25 and 25/12/2024. """

'''
(\d{2}/\d{2}/\d{4}) matches the DD/MM/YYYY 12/09/2024
(\d{4}-\d{2}-\d{2}) matches the YYYY-MM-DD format 2024/09/12
([A-Za-z]{3,9} \d{1,2}, \d{4}) matches the Month DD, YYYY format Sep 12, 2023 or August 15, 2022
'''
pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|([A-Za-z]{3,9} \d{1,2}, \d{4})'

dates = re.findall(pattern, text)
extracted_dates = []
for date_tuple in dates:
    for date in date_tuple:
        if date:  
            extracted_dates.append(date)

print("Extracted dates:")
for date in extracted_dates:
    print(date)


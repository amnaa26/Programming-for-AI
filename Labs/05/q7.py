#Programmer: Amna(23k-0066)
#Date: 18th Sept 2024

import re

text = """ Hello, you can reach out to us at support@example.com or sales@example.co.uk.
        For more information, contact john.doe123@example.org or jane_doe@example.com.
        Invalid emails: hello@world, test@com, @missingusername.com """

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
emails = re.findall(pattern, text)
print("Extracted email addresses: ")
for email in emails:
    print(email)
# Programmer: Amna(23k-0066)
# Date: 28/Aug/2024
# Q3) Ask user to enter his URL that should starts with http://www.( user url ) and then convert it into user url.com

user = input("Enter URL that should start with http://www.: ")
prefix = "http://www."
suffix = ".com"

# Check if the URL starts with the correct prefix
if user.startswith(prefix):
    user_without_prefix = user[len(prefix):]
    result_url = user_without_prefix + suffix
    print("Converted URL:", result_url)
else:
    print("Entered URL is not according to the format")
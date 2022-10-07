import re

def Valid1(email):

    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern,email):

        return "Valid"

    else:

        return "Invalid"

email = input("Enter your email to verify whether it is valid or not : ")

print(Valid1(email))
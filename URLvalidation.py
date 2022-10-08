import re

def check_URL(input_URL):

    reg = ("(http|https)://(www.)?" + "[a-zA-Z0-9:%._\\+~#?&//=]" +

          "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)")

    exp = re.compile(reg)

    if (input_URL == None):

        print("Input string is empty")

    if(re.search(exp,input_URL)):

        print("Input URL is valid!")

    else:

        print("Input URL is inval;id!")

input_URL = input("Enter any URL to verify whether it is valid or not : ")

check_URL(input_URL)

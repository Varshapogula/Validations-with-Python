
import re

regex = '^[A-Za-z_][A-Za-z0-9_]*'
     
def check(string):
 
    if(re.search(regex, string)) and len(string)<257:

        print("Valid Identifier")
         
    else:

        print("Invalid Identifier")
     
if __name__ == '__main__' :
     
    string = input("enter a string to check whether it is valid identifier or not : ")

    check(string)

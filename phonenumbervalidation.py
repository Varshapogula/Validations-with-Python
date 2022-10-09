import re
 
def isValid(s):
     
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")

    return Pattern.match(s)
 
# Driver Code

s = input("Enter a phone Number to check valid or not : ")

if (isValid(s)):

    print ("Valid Number")   

else :
    
    print ("Invalid Number")
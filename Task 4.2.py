#Day4
#Question 2 :
#Create a function that can identify if the given input is an email or phone number using regex
import re
def identify(get):
    email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mobno = r'^\+?[0-9]{10,15}$'
    get = str(get)
    if re.match(email, get):
        return "The input ",get," is an Email."
    elif re.match(mobno, get):
        return "The input ",get," is a Mobile Number."
    else:
        return "The input ",get," is neither an Email nor a Mobile Number."
print(identify("adityenh@gmail.com"))
print(identify(9876543210))
print(identify("CODE SPRINT: EXPLORING PYTHON"))


import re

def main():
    username = input("username: ")
    password = input("password: ")

    result = bool(re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-z\d]{8,}", password))

    if result: 
        print("succesfully registered")
    else:
        print("password not okay, 8chars, upper, lower, digit")

main()

password = ""
#Requirements 
#One Capital
#eight characters
#one number
#one symbol
print("Please enter a password to check")
print("Password must contain, 1 capital, at least 8 characters, one number and one symbol!@#$%^&*()")
password = input()

def passwordchecker(password):
    symbols = "!@#$%^&*()"
    capital = False
    charlength = False
    number = False
    symbol = False
    if len(password) < 8:
        print("Password invalid.")
        return False
    else:
        charlength = True
        for char in password:
            if char.isnumeric():
                number = True
            else:
                pass
            if char in symbols:
                symbol = True
            else:
                pass
            if char.isupper():
                capital = True
            else:
                pass
        if capital == False or charlength == False or number == False or symbol == False:
            print("Password invalid")
            return False
        else:
            print("Password Valid")
            return True

result = passwordchecker(password)
print(result)


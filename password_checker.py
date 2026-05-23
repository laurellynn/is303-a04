'''
Laurel Lynn 
IS 303 - A04

Password Checker

This program will check if a new password
created has good strength and protection

Inputs: 
- Password (str)

Processes:
- Check length: 
    length(prompt): keeps asking until certain character amount hit (try/except)
- Check uppercase:
    uppercase(prompt): requires the user to use at least one upper case letter (if/else)
- Check digits:
    digits(prompt): checks to see if at least one special character was used (if/else)
- Calcualte overall strength
    calcualte_strength(length, uppercase, digits): if all are followed, score = strong, 
    if two followed, score = okay,
    if one followed, score = weak

Outputs:
- Return if password strength is weak, good, or strong
- Prompt user to adjust to make stronger
'''
### Functions
password = input(f"Create a password: (It must have the following: At least 10 digits, 1 capital letter, 1 unique character) ")
special_chars = "!@#$%^&*()_-+=[;}{:']?/>.<,|~`1234567890"
try_again = "Try again! "


def get_length(password):
    ''' Keep asking until the user enters 10 characters.'''
    while True: 
        if len(password) >= 10:
            return("Your password is long enough. ")
        else:
            print("Your password must be at least 10 characters long. ")
            print(try_again)     
            exit()      

def get_capital(password):
     while True: 
        if any(char.isupper() for char in password):
            return("Your password has at least one uppercase letter. ")
        else:
            print("You need at least one uppercase letter. ")
            print(try_again)
            exit() 
     
def get_unique(password):
     while True: 
        if any(char in special_chars for char in password):
            return("Your password has at least one unique character. ")
        else:
            print("You need at least one unique character. ")
            print(try_again) 
            exit()
     
  
def calculate_strength(length, uppercase, digits):
    ''' If all are followed, score = strong, if two followed, score = good, if one followed, score = weak.'''
    if length == "Your password is long enough. " and uppercase == "Your password has at least one uppercase letter. " and digits == "Your password has at least one unique character. ":
        return("Your password is strong! ")
    elif (length == "Your password is long enough. " and uppercase == "Your password has at least one uppercase letter. ") or (length == "Your password is long enough. " and digits == "Your password has at least one unique character. ") or (uppercase == "Your password has at least one uppercase letter. " and digits == "Your password has at least one unique character. "):
        return("Your password is okay! Try again and add either an uppercase letter or a unique character to make it stronger! ")
    elif length == "Your password is long enough. " or uppercase == "Your password has at least one uppercase letter. " or digits == "Your password has at least one unique character. ": 
        return("Your password is weak! Try again and add an uppercase letter, a unique character, and make it at least 10 characters long to make it stronger! ")

### Main
length = get_length(password)
uppercase = get_capital(password)
digits = get_unique(password)
strength = calculate_strength(length, uppercase, digits)
print(f"--- Password Strength Results---")
print(length)
print(uppercase)
print(digits)
print(strength)

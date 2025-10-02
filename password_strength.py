# this is to check the strength of a password
from string import punctuation

print (
        """ The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %)."""
    )

password = input("\nEnter your password to check its strength: ")

def check_password_strength(password):
    if len(password) < 8:
        return "length should be at least 8 characters"
    
    # for char in password:
    #     if char.isspace():
    #         return "password should not contain spaces"
    
    
    
    if not any(char.isdigit() for char in password):
        return {"password should contain at least one digit" : False}
    
    if any(char.isspace() for char in password):
        return {"password should not contain spaces" : False}

    if not any(char.isupper() for char in password):
        return {"password should contain at least one uppercase letter" : False}

    if not any(char.islower() for char in password):
        return {"password should contain at least one lowercase letter" : False}

    if not any(char in punctuation for char in password):
        return {"password should contain at least one special character" : False}

    return {"password is strong" : True}


if __name__ == "__main__":
    result = check_password_strength(password)
    print(result)
    
    

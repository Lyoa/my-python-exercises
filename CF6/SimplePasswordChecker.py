def check_password(password):
    #check for length
    if len(password) < 8:
        return False
    #check for uppercase
    if not any(char.isupper() for char in password):
        return False
    #check for lowercase
    if not any(char.islower() for char in password):
        return False
    #check for digits
    if not any(char.isdigit() for char in password):
        return False
    return True


def display(password):
    if check_password(password):
        print("That's a good password")
    else:
        print("That isn't a good password")
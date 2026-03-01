# Skills Test 3rd Quarter
from pyscript import display, document


def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    username_length = len(username)

    if username_length < 5:
        display(f'Username too short! Add at least {5 - username_length} more character/s to proceed.', target='output')
    else:
        return(True)


def password_verification(e):
    document.getElementById('output').innerHTML = ' '

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length < 6:
        display(f'Password too short! Add at least {6 - password_length} more character/s to proceed.', target='output')
    elif not password_has_letter:
        display(f'Password must contain at least one letter.', target='output')
    elif not password_has_number:
        display(f'Password must contain at least one number.', target='output')
    else:
        return(True)


def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        display(f'Account created! Welcome to the Intramurals.', target='output')
    else:
        display(f'Please Try Again', target='output')
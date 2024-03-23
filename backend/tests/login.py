# login.py


def login(username, password):
    # Predefined set of valid credentials
    valid_username = "user123"
    valid_password = "password123"

    # Check if provided username and password match
    if username == valid_username and password == valid_password:
        return True
    else:
        return False

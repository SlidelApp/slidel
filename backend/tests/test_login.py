# test_login.py
from login import login


def test_login_with_valid_credentials():
    assert login("user123", "password123") is True



def test_login_with_invalid_username():
    assert login("invalid_user", "password123") is False



def test_login_with_invalid_password():
    assert login("user123", "invalid_password") is False



def test_login_with_invalid_credentials():
    assert login("invalid_user", "invalid_password") is False

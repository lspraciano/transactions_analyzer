# Native Imports

# Created Imports
from resources.py.password.password_manager import generate_password


def test_generate_password_without_parameter():
    password = generate_password()
    assert type(password) is str
    assert len(password) == 8


def test_generate_password_with_parameter():
    password_len_expected = 10
    password = generate_password(length=password_len_expected)
    assert type(password) is str
    assert len(password) == password_len_expected


def test_generate_password_with_str_parameter():
    password = generate_password(length='123')
    assert type(password) is str
    assert len(password) == 8


def test_generate_password_with_none_parameter():
    password = generate_password(length=None)
    assert type(password) is str
    assert len(password) == 8


def test_generate_password_with_float_parameter():
    password = generate_password(length=31.5)
    assert type(password) is str
    assert len(password) == 8

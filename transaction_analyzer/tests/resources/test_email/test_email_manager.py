from resources.py.email.email_manager import (
    send_email_password_new_user,
    validate_email,
)


def test_validate_email_with_valid_email():
    assert validate_email(email='TEST@GMAIL.COM') is True


def test_validate_email_with_invalid_email():
    assert validate_email(email='TESTGMAIL.COM') is False


def test_validate_email_with_none():
    assert validate_email(email=None) is False


def test_validate_email_with_integer():
    assert validate_email(email=11) is False


def test_validate_email_with_list():
    assert validate_email(email=['1', 2]) is False


def test_send_email_valid_email_and_password(app):
    with app.app_context():
        assert 'success' in send_email_password_new_user(
            email='TEST@GMAIL.COM', password='abcd1234'
        )


def test_send_email_valid_email(app):
    with app.app_context():
        assert 'success' in send_email_password_new_user(
            email='TEST@GMAIL.COM', password='abcd1234'
        )


def test_send_email_invalid_email():
    assert 'error' in send_email_password_new_user(
        email='TESTGMAIL.COM', password='abcd1234'
    )


def test_send_email_with_email_not_string():
    assert 'error' in send_email_password_new_user(
        email=111, password='abcd1234'
    )


def test_send_email_with_email_none():
    assert 'error' in send_email_password_new_user(
        email=None, password='abcd1234'
    )


def test_send_email_with_password_not_string():
    assert 'error' in send_email_password_new_user(
        email='TEST@GMAIL.COM', password=111
    )


def test_send_email_with_password_none():
    assert 'error' in send_email_password_new_user(
        email='TEST@GMAIL.COM', password=None
    )

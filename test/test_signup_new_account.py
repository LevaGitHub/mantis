from fixture.general import generate_sequence
import string


def test_signup_new_account(app):
    username = "user_{}".format(generate_sequence(10, string.ascii_letters))
    password = "test"
    email = username + "@localhost"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    assert app.soap.can_login(username, password)

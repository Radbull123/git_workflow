from src.hello_world import hello_user, hello_world


def test_hello_user_if_not_exists():
    """The 'Unknown User' should be appeared if username is not set in environment"""
    assert hello_user() == "Hello Unknown User", "Invalid username, should be: 'Unknown User'"


def test_hello_world():
    assert hello_world() == "Hello World"


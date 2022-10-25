from src.hello_world import hello_user, hello_world


def test_hello_user():
    assert hello_user() == 'Hello User'


def test_hello_world():
    assert hello_world() == "Hello World"

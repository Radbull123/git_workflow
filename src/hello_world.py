import os


def hello_user() -> str:
    os_variable_name = os.environ.get("TEST_NAME", "User")
    return f"Hello {os_variable_name}"


def hello_world() -> str:
    return "Hello World"

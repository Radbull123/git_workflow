import os


def hello_user() -> str:
    # Second item is the default string if first value is not found in environment
    os_variable_name = os.environ.get("TEST_NAME", "Unknown User")
    return f"Hello {os_variable_name}"


def hello_world() -> str:
    return "Hello World"

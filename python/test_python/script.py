import os


def say_hello():
    user = os.getenv("USER")
    print(f"Hello, {user}!")


say_hello()

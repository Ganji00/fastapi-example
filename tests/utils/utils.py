import random
import string


def random_string() -> str:
    """
    Generates a random string of 10 characters.
    """
    return "".join(random.choices(string.ascii_letters, k=10))

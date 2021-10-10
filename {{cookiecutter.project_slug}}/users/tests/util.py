import string
import random


def generate_random_string() -> str:
    result = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=8)
    )
    return result

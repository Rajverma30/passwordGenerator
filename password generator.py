import random
import string
def generate_password(length):
    characters = string.ascii.letters + string.digits + string.punctuation
    password=' ',join(random.choice(characters) for _ in range(length) )

    return password

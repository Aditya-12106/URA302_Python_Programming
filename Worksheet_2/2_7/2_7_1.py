import random
import string

characters = string.ascii_letters + string.digits

for _ in range(100):
    length = random.randint(6, 8)

    random_string = ""

    for _ in range(length):
        random_string += random.choice(characters)

    print(random_string)
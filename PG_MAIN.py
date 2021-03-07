import string
import numpy as np

def generate_password(length):
    lcase = list(string.ascii_lowercase)
    ucase = list(string.ascii_uppercase)
    numbers = list(string.digits)
    punct = list(string.punctuation)

    all_chars = lcase + ucase + numbers + punct
    generated_pwd = list()

    for i in range(length):
        generated_pwd.append(np.random.choice(all_chars))   

    print(generated_pwd)

    return("".join(generated_pwd))

print("asas")
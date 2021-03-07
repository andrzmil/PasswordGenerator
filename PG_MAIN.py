import string
import numpy as np

def generate_password(length, lc, uc, nb, pct):
    lcase = list(string.ascii_uppercase)
    ucase = list(string.ascii_lowercase)
    numbers = list(string.digits)
    punct = list(string.punctuation)

    all_chars = lcase + ucase + numbers + punct
    generated_pwd = list()

    for i in range(length-lc-uc-nb-pct):
        generated_pwd.append(np.random.choice(all_chars))   

    for i in range(lc):
        generated_pwd.append(np.random.choice(lcase)) 

    for i in range(uc):
        generated_pwd.append(np.random.choice(ucase))

    for i in range(nb):
        generated_pwd.append(np.random.choice(numbers)) 

    for i in range(pct):
        generated_pwd.append(np.random.choice(punct))

    np.random.shuffle(generated_pwd)
    

    return("".join(generated_pwd))



print("asas")
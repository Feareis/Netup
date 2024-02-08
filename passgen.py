import random
import string

lmin = int(input("minimum password length : "))
lmax = int(input("maximum password length (default 13) : "))
sp = input("special characters in your password (Yes/No | y/n)").lower() == 'Yes' or 'y'


def gen(length, sp=True, lmin=8):
    caracteres = string.ascii_letters + string.digits
    if sp:
        caracteres += string.punctuation
    length = max(lmin, lmax)
    mot_de_passe = ''.join(random.choice(caracteres) for i in range(length))
    return mot_de_passe


passgen = gen(lmax, sp, lmin)

print("Pass :", passgen)
import random
import string

def passwordGenerator():
    possibilities = string.ascii_letters + string.digits + "!#$%^&*()-_/"

    password = ''
    for i in range(10):
        password += random.choice(possibilities)
    return password

passwordKey = passwordGenerator()

print("Password: " + passwordKey)



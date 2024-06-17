import random
import string

def passwordGenerator():
    possibilities = string.ascii_letters + string.digits + string.digits

    password = ''
    for i in range(10):
        password += random.choice(possibilities)
    return password

passwordKey = passwordGenerator()

print("Password: " + passwordKey)



# Write a password generator in Python.

import random

length = int(input("How long do you want your password to be? "))

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_-?"

password = "".join(random.sample(characters, length))

print(password)

import random
import time
import os

def generate_password():
    password = ""
    for i in range(6):
        password += str(random.randint(0, 9))
    return password


time_left = 6  # Can be changed to any number

print(generate_password())
print("-" * 20)

while True:
    time_left -= 1
    time.sleep(1)
    print("Time Left :", time_left)

    if time_left == 0:
        os.system("cls") # Clear console
        print(generate_password())
        print("-" * 20)
        time_left = 6

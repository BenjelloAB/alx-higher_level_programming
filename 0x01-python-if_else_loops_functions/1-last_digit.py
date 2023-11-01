#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = (-number) % 10
    n = -n
else:
    n = number % 10
if number % 10 == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n < 6 and n != 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
elif number % 10 > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")

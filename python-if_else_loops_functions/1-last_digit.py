#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)

if number < 0:
    thelastd = -1 * number % 10
    thelastd = -1 * thelastd

else:
    thelastd = number % 10


if thelastd > 5:
    print(f"Last digit of {number} is {thelastd} and is greater than 5")

elif thelastd == 0:
    print(f"Last digit of {number} is {thelastd} and is 0")

else:
    print(f"Last digit of {number} is {thelastd} and is less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_num = -(abs(number) % 10)
else:
    new_num = abs(number) % 10

output = f"Last digit of {number} is {new_num}"
if new_num > 0:
    output += " and is greater than 5"
elif new_num == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)

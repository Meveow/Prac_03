import random

amount = int(input("How many quick picks? "))

for line in range(amount):
    line = random.randint(1, 45)
    print(line)

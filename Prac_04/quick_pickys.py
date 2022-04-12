import random

COLUMN = 6

amount = int(input("How many quick picks? "))

for c in range(amount):
    values = []
    for r in range(COLUMN):
        num = random.randint(1, 45)
        while num in values: #no repitition of numbers
            num = random.randint(1, 45)
        values.append(num)
    values.sort()
    print(" ".join(str(r) for r in values))
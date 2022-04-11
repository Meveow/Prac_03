import random
VALUES = []

amount = int(input("How many quick picks? "))

for line in range(amount):
    line = random.randint(1, 45)
    for line in range(6):
        line = random.randint(1, 45)
        VALUES.append(line)
        VALUES.sort()
        print(VALUES)
        # print(line, end=' ')

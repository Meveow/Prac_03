import random

LINE = 6

amount = int(input("How many quick picks? "))

for c in range(amount): #number of lines
    values = []
    for r in range(LINE): #six elements in each line
        num = random.randint(1, 45)
        while num in values: #no repitition of numbers
            num = random.randint(1, 45)
        values.append(num)
    values.sort()
    print(" ".join(str(r) for r in values))
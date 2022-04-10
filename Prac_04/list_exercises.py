numbers = []

times = 5

for n in range(times):
    response = int(input("Number: "))
    numbers.append(response)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / times}")
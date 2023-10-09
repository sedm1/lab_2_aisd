numbers = [3, 17, 6, 20, 1]
l = len(numbers)
for round in range(l - 1):
    for i in range(l - round - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
print(numbers)
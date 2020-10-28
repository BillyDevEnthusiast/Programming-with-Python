factor = int(input())
count = int(input())

numbers = []
data = 0

for number in range(count):
    data += factor
    numbers.append(data)
print(numbers)

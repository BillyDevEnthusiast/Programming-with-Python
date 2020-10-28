n = int(input())
capacity = 255

total_liters = 0

for i in range(n):
    liters = int(input())
    if total_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters
print(total_liters)

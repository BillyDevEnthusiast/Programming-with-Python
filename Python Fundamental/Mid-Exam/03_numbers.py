numbers = list(map(int, input().split()))

new_list = []

average_of_numbers = sum(numbers) / len(numbers)

for num in range(len(numbers)):
    if numbers[num] > average_of_numbers:
        new_list.append(numbers[num])

new_list = sorted(new_list)
new_list.sort(reverse=True)

res = []

for i in range(len(new_list)):
    if i == 5:
        break
    res.append(new_list[i])

if len(res) > 0:
    print(" ".join(map(str, res)))
else:
    print("No")

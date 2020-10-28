import math
list_numbers = list(map(int, input().split(", ")))

max_number = max(list_numbers)
number_groups = math.ceil(max_number / 10)

for groups in range(1, number_groups + 1):
    current_range = []
    for number in list_numbers:
        upper_number = groups * 10
        lower_number = upper_number - 10
        if lower_number < number <= upper_number:
            current_range.append(number)
    print(f"Group of {groups * 10}'s: {current_range}")

numbers = list(map(int, input().split(" ")))

command = input()
while command != "End":
    list_commands = command.split(" ")
    action = list_commands[0]
    index = int(list_commands[1])

    if action == "Shoot" and 0 <= index <= len(numbers) - 1:
        power = int(list_commands[2])
        numbers[index] -= power
        if numbers[index] <= 0:
            numbers.remove(numbers[index])

    elif action == "Add":
        value = int(list_commands[2])

        if 0 <= index <= len(numbers) - 1:
            numbers.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(list_commands[2])
        radius_start = index - radius
        radius_end = index + radius
        if (len(numbers) - 1) >= radius_start >= 0 and 0 < radius_end <= len(numbers) - 1:
            del numbers[radius_start:radius_end + 1]
        else:
            print("Strike missed!")

    command = input()

print("|".join(map(str, numbers)))

initial_array_val = list(map(int, input().split()))

while True:
    commands_list = input().split()
    commands = commands_list

    if "end" in commands_list:
        break
    elif "swap" in commands_list:
        index1 = int(commands[1])
        index2 = int(commands[2])

        initial_array_val[index1], initial_array_val[index2] = initial_array_val[index2], initial_array_val[index1]

    elif "multiply" in commands_list:
        index1 = int(commands[1])
        index2 = int(commands[2])

        initial_array_val[index1] = initial_array_val[index1] * initial_array_val[index2]

    elif "decrease" in commands_list:
        for i in range(len(initial_array_val)):
            initial_array_val[i] -= 1

print(", ".join(map(str, initial_array_val)))

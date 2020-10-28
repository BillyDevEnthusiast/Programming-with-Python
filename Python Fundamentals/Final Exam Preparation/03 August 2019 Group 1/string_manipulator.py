string = input()

command_list = input()

while command_list != "End":
    args = command_list.split()
    command = args[0]

    if command == "Translate":
        char = args[1]
        replacement = args[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == "Includes":
        word = args[1]

        if word in string:
            print("True")
        else:
            print("False")
    elif command == "Start":
        word = args[1]
        print(string.startswith(word))
    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = args[1]
        if char in string:
            print(string.rindex(char))
        else:
            command_list = input()
            continue
    elif command == "Remove":
        startIndex = int(args[1])
        count = int(args[2])
        if startIndex >= 0 and (startIndex + count) <= (len(string) - 1):
            part1 = string[:startIndex]
            part2 = string[startIndex + count:]
            string = part1 + part2
            print(string)

    command_list = input()

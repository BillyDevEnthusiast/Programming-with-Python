word = input()

command_list = input()

while command_list != "Finish":
    args = command_list.split()
    command = args[0]

    if len(word) == 0:
        break

    if command == "Replace":
        currentChar = args[1]
        newChar = args[2]
        word = word.replace(currentChar, newChar)

        if len(word) == 0:
            break
        print(word)
    elif command == "Cut":
        startIndex = int(args[1])
        endIndex = int(args[2])

        if startIndex >= 0 and endIndex <= (len(word) - 1):
            part1 = word[:startIndex]
            part2 = word[endIndex + 1:]
            word = part1 + part2

            if len(word) == 0:
                break
            print(word)
        else:
            print("Invalid indexes!")

        part1 = word[:startIndex]
        part2 = word[endIndex + 1:]
        word = part1 + part2

        if len(word) == 0:
            break
    elif command == "Make":
        size = args[1]

        if size == "Upper":
            word = word.upper()
        elif size == "Lower":
            word = word.lower()
        print(word)
    elif command == "Check":
        string = args[1]
        if string in word:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command == "Sum":
        startIndex = int(args[1])
        endIndex = int(args[2])

        if startIndex >= 0 and endIndex <= (len(word) - 1):
            substring = word[startIndex:endIndex + 1]
            ascii_value = 0
            for ch in substring:
                ascii_value += ord(ch)
            if ascii_value > 0:
                print(ascii_value)
        else:
            print("Invalid indexes!")

    command_list = input()

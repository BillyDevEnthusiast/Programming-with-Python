username = input()

command_list = input()

while command_list != "Sign up":
    args = command_list.split()
    command = args[0]

    if command == "Case":
        size = args[1]

        if size == "lower":
            username = username.lower()
        elif size == "upper":
            username = username.upper()
        print(username)
    elif command == "Reverse":
        startIndex = int(args[1])
        endIndex = int(args[2])

        if startIndex >= 0 and endIndex <= (len(username) - 1):
            substring = username[startIndex:endIndex+1]
            substring = substring[::-1]
            print(substring)
        else:
            command_list = input()
            continue
    elif command == "Cut":
        substring = args[1]

        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = args[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        char = args[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")

    command_list = input()

password = input()

command_list = input()

while command_list != "Done":
    command_list = command_list.split()
    command = command_list[0]

    if command == "TakeOdd":
        password_new = ""
        for i in range(len(password)):
            if i % 2 != 0:
                password_new += password[i]
        password = password_new
        print(password)

    elif command == "Cut":
        start_index = int(command_list[1])
        end_index = start_index + int(command_list[2])
        password = password[:start_index] + password[end_index:]
        print(password)
    elif command == "Substitute":
        substring = command_list[1]
        new_substring = command_list[2]

        if substring not in password:
            print("Nothing to replace!")
            command_list = input()
            continue
        password = password.replace(substring, new_substring)
        print(password)

    command_list = input()

print(f"Your password is: {password}")

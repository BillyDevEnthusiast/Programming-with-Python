encrypted_message = input()

command_list = input()

while command_list != "Decode":
    args = command_list.split("|")
    command = args[0]

    if command == "Move":
        number_letters = int(args[1])
        part1 = encrypted_message[:number_letters]
        part2 = encrypted_message[number_letters:]
        encrypted_message = part2 + part1
    elif command == "Insert":
        index = int(args[1])
        value = args[2]
        if 0 <= index <= (len(encrypted_message) - 1):
            part1 = encrypted_message[:index]
            part2 = encrypted_message[index:]
            encrypted_message = part1 + value + part2
        else:
            encrypted_message = encrypted_message + value
    elif command == "ChangeAll":
        substring = args[1]
        replacement = args[2]
        if substring in encrypted_message:
            encrypted_message = encrypted_message.replace(substring, replacement)
        else:
            command_list = input()
            continue

    command_list = input()

print(f"The decrypted message is: {encrypted_message}")

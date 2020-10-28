concealed_message = input()

command_set = input()
while command_set != "Reveal":
    command_set = command_set.split(":|:")
    command = command_set[0]

    if command == "ChangeAll":
        letter_to_be_replaced = command_set[1]
        letter = command_set[2]

        if letter_to_be_replaced not in concealed_message:
            command_set = input()
            continue
        concealed_message = concealed_message.replace(letter_to_be_replaced, letter)
        print(concealed_message)

    if command == "Reverse":
        sub_string = (command_set[1])
        if sub_string not in concealed_message:
            print("error")
            command_set = input()
            continue
        
        concealed_message = concealed_message.replace(sub_string, "", 1)
        sub_string = sub_string[::-1]
        concealed_message += sub_string
        print(concealed_message)

    if command == "InsertSpace":
        index = int(command_set[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)

    command_set = input()

print(f"You have a new text message: {concealed_message}")

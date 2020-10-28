raw_activation_key = input()

commands_list = input()

while commands_list != "Generate":
    args = commands_list.split(">>>")
    command = args[0]

    if command == "Contains":
        substring = args[1]

        if substring not in raw_activation_key:
            print("Substring not found!")
            commands_list = input()
            continue
        print(f"{raw_activation_key} contains {substring}")

    elif command == "Flip":
        cap_low = args[1]
        start_index = int(args[2])
        end_index = int(args[3])
        part_1 = raw_activation_key[:start_index]
        part_2 = raw_activation_key[end_index:]
        substring1 = raw_activation_key[start_index:end_index]

        if cap_low == "Upper":
            substring1 = substring1.upper()
            raw_activation_key = part_1 + substring1 + part_2
        elif cap_low == "Lower":
            substring1 = substring1.lower()
            raw_activation_key = part_1 + substring1 + part_2
        print(raw_activation_key)

    elif command == "Slice":
        start_index = int(args[1])
        end_index = int(args[2])
        substring1 = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(substring1, "")
        print(raw_activation_key)

    commands_list = input()

print(f"Your activation key is: {raw_activation_key}")

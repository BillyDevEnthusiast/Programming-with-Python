skill = input()

command_list = input()

while command_list != "For Azeroth":
    args = command_list.split()

    if "GladiatorStance" in command_list:
        skill = skill.upper()
        print(skill)
    elif "DefensiveStance" in command_list:
        skill = skill.lower()
        print(skill)
    elif "Dispel" in command_list:
        index = int(args[1])
        letter = args[2]

        if index > len(skill) - 1 or index < 0:
            print("Dispel too weak.")
            command_list = input()
            continue
        skill = skill.replace(skill[index], letter, 1)
        print("Success!")

    elif "Target Change" in command_list:
        substring = args[2]
        second_substring = args[3]
        skill = skill.replace(substring, second_substring)
        print(skill)

    elif "Target Remove" in command_list:
        substring = args[2]
        skill = skill.replace(substring, "")
        print(skill)
    else:
        print("Command doesn't exist!")
        command_list = input()
        continue

    command_list = input()

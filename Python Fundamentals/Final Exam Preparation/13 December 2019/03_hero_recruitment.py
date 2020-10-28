heroes = {}
command_list = input()

while command_list != "End":
    args = command_list.split()
    command = args[0]
    hero = args[1]

    if command == "Enroll":
        if hero in heroes:
            print(f"{hero} is already enrolled.")
            command_list = input()
            continue
        heroes[hero] = []
    elif command == "Learn":
        spell = args[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
            command_list = input()
            continue
        if spell in heroes[hero]:
            print(f"{hero} has already learnt {spell}.")
            command_list = input()
            continue
        heroes[hero].append(spell)
    elif command == "Unlearn":
        spell = args[2]
        if hero not in heroes:
            print(f"{hero} doesn't exist.")
            command_list = input()
            continue
        if spell not in heroes[hero]:
            print(f"{hero} doesn't know {spell}.")
            command_list = input()
            continue
        heroes[hero].remove(spell)

    command_list = input()

heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))
print("Heroes:")
for key, value in heroes.items():
    print(f"== {key}: {', '.join(value)}")

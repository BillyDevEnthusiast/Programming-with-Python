command_list = input()
guests_list = {}
unliked_meals = 0
while command_list != "Stop":
    command, guest, meal = command_list.split("-")

    if command == "Like":
        if guest not in guests_list:
            guests_list[guest] = []
        if meal in guests_list[guest]:
            command_list = input()
            continue
        guests_list[guest].append(meal)
    elif command == "Unlike":
        if guest not in guests_list:
            print(f"{guest} is not at the party.")
            command_list = input()
            continue
        if meal not in guests_list[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
            command_list = input()
            continue
        guests_list[guest].remove(meal)
        print(f"{guest} doesn't like the {meal}.")
        unliked_meals += 1

    command_list = input()

guests_list = dict(sorted(guests_list.items(), key=lambda x: (-len(x[1]), x[0])))
for k, v in guests_list.items():
    print(f"{k}: {', '.join(v)}")
print(f"Unliked meals: {unliked_meals}")

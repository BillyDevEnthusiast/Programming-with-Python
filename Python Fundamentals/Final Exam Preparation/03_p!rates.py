cities = {}
data_list = input()

while data_list != "Sail":
    args = data_list.split("||")
    city = args[0]
    population = int(args[1])
    gold = int(args[2])

    if city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
        data_list = input()
        continue

    cities[city] = {}
    cities[city]["population"] = population
    cities[city]["gold"] = gold

    data_list = input()

command_list = input()

while command_list != "End":
    tokens = command_list.split("=>")
    command = tokens[0]
    city = tokens[1]

    if command == "Plunder":
        people = int(tokens[2])
        gold = int(tokens[3])
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            print(f"{city} has been wiped off the map!")
            del cities[city]
            command_list = input()
            continue

    elif command == "Prosper":
        gold = int(tokens[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command_list = input()
            continue
        cities[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

    command_list = input()

if len(cities) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    sorted_cities = sorted(cities.keys(), key=lambda c: (-cities[c]["gold"], c))
    for x in sorted_cities:
        print(f"{x} -> Population: {cities[x]['population']} citizens, Gold: {cities[x]['gold']} kg")

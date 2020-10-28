list_rooms = input().split("|")

health = 100
bitcoin = 0
commands = []
not_dead = True
counter = 0
for room in range(0, len(list_rooms)):
    commands = list_rooms[room].split(" ")
    action = commands[0]
    number = int(commands[1])

    if action == "potion":
        counter = +1
        temp = health
        health += number
        healed = number

        if health > 100:
            health = 100
            healed = health - temp
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        counter = +1
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        monster = commands[0]
        counter = +1
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room + 1}")
            not_dead = False
            break

if not_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")

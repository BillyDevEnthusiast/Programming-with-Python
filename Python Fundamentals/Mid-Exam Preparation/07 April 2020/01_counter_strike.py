energy = int(input())

counter = 0
energy_not_enough = False

command = input()
while True:

    if command == "End of battle":
        break

    else:
        distance = int(command)
        if distance <= energy:
            energy -= distance
            counter += 1
            if counter % 3 == 0:
                energy += counter
        else:
            energy_not_enough = True
            print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
            break
    command = input()

if not energy_not_enough:
    print(f"Won battles: {counter}. Energy left: {energy}")

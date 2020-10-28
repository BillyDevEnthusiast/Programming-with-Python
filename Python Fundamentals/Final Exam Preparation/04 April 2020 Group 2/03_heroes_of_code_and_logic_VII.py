n = int(input())

heroes = {}

for items in range(n):
    heroes_list = input().split()
    hero = heroes_list[0]
    hit_points = int(heroes_list[1])
    mana_points = int(heroes_list[2])

    heroes[hero] = {}
    heroes[hero]["HP"] = hit_points
    heroes[hero]["MP"] = mana_points

command_list = input()

while command_list != "End":
    tokens = command_list.split(" - ")
    command = tokens[0]
    hero = tokens[1]

    if command == "CastSpell":
        mp_needed = int(tokens[2])
        spell_name = tokens[3]

        if heroes[hero]["MP"] < mp_needed:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
            command_list = input()
            continue
        heroes[hero]["MP"] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")

    elif command == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes[hero]["HP"] -= damage

        if heroes[hero]["HP"] <= 0:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]
            command_list = input()
            continue

        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")

    elif command == "Recharge":
        MP_amount_to_recharge = int(tokens[2])
        current_MP = heroes[hero]["MP"]
        MP_to_recharge = 0
        if current_MP + MP_amount_to_recharge > 200:
            MP_to_recharge = 200 - current_MP
            heroes[hero]["MP"] = 200
        else:
            MP_to_recharge = MP_amount_to_recharge
            heroes[hero]["MP"] += MP_to_recharge

        print(f"{hero} recharged for {MP_to_recharge} MP!")

    elif command == "Heal":
        HP_amount_to_heal = int(tokens[2])
        current_HP = heroes[hero]["HP"]
        HP_to_heal = 0

        if heroes[hero]["HP"] + HP_amount_to_heal <= 100:
            heroes[hero]["HP"] += HP_amount_to_heal
            HP_to_heal = HP_amount_to_heal
        else:
            HP_to_heal = 100 - current_HP
            heroes[hero]["HP"] = 100

        print(f"{hero} healed for {HP_to_heal} HP!")

    command_list = input()

sorted_heroes = sorted(heroes.keys(), key=lambda c: (-heroes[c]["HP"], c))
for x in sorted_heroes:
    print(x)
    print(f"HP: {heroes[x]['HP']}")
    print(f"MP: {heroes[x]['MP']}")

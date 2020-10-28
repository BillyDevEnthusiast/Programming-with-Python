import re

n = int(input())

pattern = r"^\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#$"

for i in range(n):
    text = input()
    valid_names = re.findall(pattern, text)

    if len(valid_names) == 0:
        print("Access denied!")
        continue

    for j in valid_names:
        name = j[0]
        position = j[1]
        strength = len(name)
        armour = len(position)
    print(f"""{name}, The {position}
>> Strength: {strength}
>> Armour: {armour}""")

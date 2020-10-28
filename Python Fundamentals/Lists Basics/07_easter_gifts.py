list_gifts = input().split()

commands = input()

while commands != "No Money":
    command_list = commands.split()
    command = command_list[0]
    gift = command_list[1]

    if command == "OutOfStock":
        for i in range(len(list_gifts)):
            if list_gifts[i] == gift:
                list_gifts[i] = "None"
    elif command == "Required":
        index = command_list[2]
        index_num = int(index)
        if 0 <= index_num < len(list_gifts):
            list_gifts[index_num] = gift
    elif command == "JustInCase":
        list_gifts[-1] = gift
    commands = input()

to_remove = "None"

for k in list_gifts:
    if to_remove in list_gifts:
        list_gifts.remove(to_remove)
gifts_final = " ".join(list_gifts)

print(gifts_final)

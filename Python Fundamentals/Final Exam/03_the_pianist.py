n = int(input())
music = {}
for i in range(n):
    data = input()
    tokens = data.split("|")
    piece = tokens[0]
    composer = tokens[1]
    key = tokens[2]
    music[piece] = {}
    music[piece]["composer"] = composer
    music[piece]["key"] = key

command_list = input()

while command_list != "Stop":
    args = command_list.split("|")
    command = args[0]
    piece = args[1]

    if command == "Add":
        composer = args[2]
        key = args[3]
        if piece not in music:
            music[piece] = {}
            music[piece]["composer"] = composer
            music[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
            command_list = input()
            continue
    elif command == "Remove":
        if piece in music:
            del music[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            command_list = input()
            continue
    elif command == "ChangeKey":
        if piece in music:
            new_key = args[2]
            music[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
            command_list = input()
            continue

    command_list = input()

sorted_music = sorted(music.keys(), key=lambda m: (m, music[m]["composer"]))

for x in sorted_music:
    print(f"{x} -> Composer: {music[x]['composer']}, Key: {music[x]['key']}")

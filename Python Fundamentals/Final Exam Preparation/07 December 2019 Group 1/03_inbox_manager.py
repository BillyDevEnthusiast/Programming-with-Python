users = {}

command_list = input()

while command_list != "Statistics":
    args = command_list.split("->")
    command = args[0]
    username = args[1]

    if command == "Add":
        if username not in users:
            users[username] = []
        else:
            print(f"{username} is already registered")
    elif command == "Send":
        email = args[2]
        users[username].append(email)
    elif command == "Delete":
        if username not in users:
            print(f"{username} not found!")
        else:
            del users[username]

    command_list = input()

users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))

print(f"Users count: {len(users)}")
for k, v in users.items():
    print(k)
    for k in v:
        print(f" - {k}")

users = {}

command_list = input()

while command_list != "Log out":
    args = command_list.split(": ")
    command = args[0]
    username = args[1]
    if command == "New follower":
        if username not in users:
            users[username] = 0
        else:
            command_list = input()
            continue
    elif command == "Like":
        count = int(args[2])
        if username not in users:
            users[username] = 0
            users[username] += count
            command_list = input()
            continue
        users[username] += count
    elif command == "Comment":
        if username not in users:
            users[username] = 1
            command_list = input()
            continue
        users[username] += 1
    elif command == "Blocked":
        if username not in users:
            print(f"{username} doesn't exist.")
            command_list = input()
            continue
        del users[username]

    command_list = input()

users = dict(sorted(users.items(), key=lambda x: (-x[1], x[0])))

print(f"{len(users)} followers")

for k, v in users.items():
    print(f"{k}: {v}")

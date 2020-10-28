messages = {}
capacity_inbox = int(input())

command_list = input()

while command_list != "Statistics":
    args = command_list.split("=")
    command = args[0]
    username = args[1]
    if command == "Add":
        sent = int(args[2])
        received = int(args[3])
        if username not in messages:
            messages[username] = {}
            messages[username]["sent"] = sent
            messages[username]["received"] = received
        else:
            command_list = input()
            continue
    elif command == "Message":
        sender = args[1]
        receiver = args[2]
        if sender in messages and receiver in messages:
            messages[sender]["sent"] += 1
            if (messages[sender]["sent"] + messages[sender]["received"]) >= capacity_inbox:
                del messages[sender]
                print(f"{sender} reached the capacity!")
            messages[receiver]["received"] += 1
            if (messages[receiver]["received"] + messages[receiver]["sent"]) >= capacity_inbox:
                del messages[receiver]
                print(f"{receiver} reached the capacity!")
        else:
            command_list = input()
            continue
    elif command == "Empty":
        if username == "All":
            messages.clear()
            command_list = input()
            continue
        if username in messages:
            del messages[username]
        else:
            command_list = input()
            continue

    command_list = input()

sorted_messages = sorted(messages.keys(), key=lambda c: (-messages[c]["received"], c))

print(f"Users count: {len(messages)}")

for x in sorted_messages:
    print(f"{x} - {messages[x]['sent'] + messages[x]['received']}")

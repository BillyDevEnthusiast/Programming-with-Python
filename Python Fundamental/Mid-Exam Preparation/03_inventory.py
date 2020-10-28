journal_items = input().split(", ")


command = input()
while command != "Craft!":
    list_args = command.split(" - ")
    action = list_args[0]
    item = list_args[1]

    if action == "Collect":
        if item not in journal_items:
            journal_items.append(item)
        else:
            command = input()
            continue
    elif action == "Drop":
        if item in journal_items:
            journal_items.remove(item)
        else:
            command = input()
            continue
    elif action == "Combine Items":
        second_args_tokens = item.split(":")
        old_item = second_args_tokens[0]
        new_item = second_args_tokens[1]

        if old_item in journal_items:
            old_item_index = journal_items.index(old_item)
            journal_items.insert(old_item_index + 1, new_item)
        else:
            command = input()
            continue
    elif action == "Renew":
        if item in journal_items:
            journal_items.remove(item)
            journal_items.append(item)
    command = input()

print(", ".join(journal_items))

import re

pattern = r"[!]([A-Z][a-z]{2,})[!][:]\[([a-zA-Z]{8,})\]"
n = int(input())

for match in range(n):
    data = input()
    valid_message = re.findall(pattern, data)

    if len(valid_message) == 0:
        print("The message is invalid")
        continue
    for i in valid_message:
        command = i[0]
        message = i[1]
    encrypted_message = []

    for ch in message:
        ch = str(ord(ch))
        encrypted_message.append(ch)

    print(f"{command}: {' '.join(encrypted_message)}")

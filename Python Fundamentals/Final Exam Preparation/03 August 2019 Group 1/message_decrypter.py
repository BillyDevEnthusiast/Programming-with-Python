import re

pattern = r"^([$]|[%])([A-Z][a-z]{2,})\1:\s\[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"

n = int(input())

for message in range(n):
    data = input()
    valid_messages = re.findall(pattern, data)
    if len(valid_messages) == 0:
        print("Valid message not found!")
        continue
    for match in valid_messages:
        tag = match[1]
        letter1 = chr(int(match[2]))
        letter2 = chr(int(match[3]))
        letter3 = chr(int(match[4]))
        message = letter1 + letter2 + letter3
        print(f"{tag}: {message}")

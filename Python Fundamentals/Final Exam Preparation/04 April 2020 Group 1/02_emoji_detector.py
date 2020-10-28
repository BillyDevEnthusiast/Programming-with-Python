import re

pattern1 = r"[:]{2}[A-Z][a-z]{2,}[:]{2}|[\*]{2}[a-zA-Z]{3,}[\*]{2}"
pattern2 = r"([0-9]+)"
data = input()
valid_emojis = re.findall(pattern1, data)
numbers_ascii = re.findall(pattern2, data)

numbers_total = ""

for num in numbers_ascii:
    numbers_total += num

cool_threshold = 1

for i in numbers_total:
    i = int(i)
    cool_threshold *= i


print(f"Cool threshold: {cool_threshold}")

cool_emoji = []

for j in valid_emojis:
    sum_ch = 0
    for ch in j:
        if ch == "*" or ch == ":":
            continue
        sum_ch += ord(ch)

    if sum_ch > cool_threshold:
        cool_emoji.append(j)

print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
print(*cool_emoji,sep='\n')

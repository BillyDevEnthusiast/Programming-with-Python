text = input()

occurences = {}

for ch in text:
    if ch == " ":
        continue

    if ch not in occurences:
        occurences[ch] = 0

    occurences[ch] += 1

for key, value in occurences.items():
    print(f"{key} -> {value} ")

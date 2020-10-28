data = input()

for i in range(len(data)):
    ch = data[i]

    if i + 1 == len(data):
        print(ch, end="")
        break

    next_ch = data[i + 1]

    if ch != next_ch:
        print(ch, end="")

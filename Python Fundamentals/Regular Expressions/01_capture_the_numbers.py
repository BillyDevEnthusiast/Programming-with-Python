import re

regex = "\d+"
res = []
while True:
    text = input()
    if not text:
        break

    data = re.findall(regex, text)
    if data != []:
        res += data

print(" ".join(res))

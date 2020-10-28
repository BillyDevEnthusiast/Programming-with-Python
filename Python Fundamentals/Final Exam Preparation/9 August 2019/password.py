import re

pattern = r"(.+)>([0-9]{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1"

n = int(input())

for match in range(n):
    data = input()
    valid_password = re.findall(pattern, data)
    if len(valid_password) == 0:
        print("Try another password!")
        continue
    for i in valid_password:
        part1 = i[1]
        part2 = i[2]
        part3 = i[3]
        part4 = i[4]
        password = part1 + part2 + part3 + part4
    print(f"Password: {password}")

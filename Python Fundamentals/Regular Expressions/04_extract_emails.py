import re

user_pattern = r"( |^)[a-zA-Z]+((\.|_|-)[a-zA-Z]+)*"
host_pattern = r"[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"

pattern = rf"{user_pattern}@{host_pattern}"

text = input()

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])

import re

pattern = f"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0), end=" ")

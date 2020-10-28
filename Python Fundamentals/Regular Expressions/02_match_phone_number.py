import re

pattern = r"(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b"

text = input()

phones = re.findall(pattern, text)

print(", ".join(phones))

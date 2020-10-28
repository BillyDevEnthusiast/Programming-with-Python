import re

pattern = r"(w{3})\.([a-zA-Z0-9-]+(-[a-zA-Z0-9-]+)*)(\.[a-z]+)+"
text = input()
while True:
    if not text:
        break

    emails = re.finditer(pattern, text, re.MULTILINE)

    for match in emails:
        print(match.group())

    text = input()

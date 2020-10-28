import re

text = input()

pattern = r"(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})"

for match in re.findall(pattern, text):
    date, separator, month, year = match
    print(f"Day: {date}, Month: {month}, Year: {year}")

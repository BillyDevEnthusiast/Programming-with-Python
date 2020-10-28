import re

pattern = r"(#|\|)([a-zA-z\s*]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1"

data = input()

valid_foods = re.findall(pattern, data)
total_calories = 0

for i in valid_foods:
    calories = int(i[3])
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in valid_foods:
    item = food[1]
    date = food[2]
    calories = food[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")

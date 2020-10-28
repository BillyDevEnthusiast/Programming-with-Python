import re

pattern = r">>([a-zA-Z]+)<<([0-9]+(\.[0-9]+)?)!([0-9]+)"

text = input()
print("Bought furniture:")

total_cost = 0

while text != "Purchase":
    match = re.fullmatch(pattern, text)

    if match is None:
        text = input()
        continue
    print(match[1])

    price = float(match[2])
    quantity = int(match[4])
    cost = price * quantity
    total_cost += cost

    text = input()

print(f"Total money spend: {total_cost:.2f}")

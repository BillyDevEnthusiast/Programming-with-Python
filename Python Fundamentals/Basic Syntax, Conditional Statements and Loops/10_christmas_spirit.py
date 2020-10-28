PRICE_ORNAMENT_SET = 2
PRICE_TREE_SKIRT = 5
PRICE_GARLANDS = 3
PRICE_TREE_LIGHTS = 15

quantity = int(input())
days = int(input())

christmas_spirit = 0
budget = 0
days_count = 1

while days_count <= days:
    if days_count % 11 == 0:
        quantity += 2
    if days_count % 2 == 0:
        budget += PRICE_ORNAMENT_SET * quantity
        christmas_spirit += 5
    if days_count % 3 == 0:
        budget += PRICE_TREE_SKIRT * quantity + PRICE_GARLANDS * quantity
        christmas_spirit += 13
    if days_count % 5 == 0:
        budget += PRICE_TREE_LIGHTS * quantity
        christmas_spirit += 17
    if days_count % 15 == 0:
        christmas_spirit += 30
    if days_count % 10 == 0:
        christmas_spirit -= 20
        budget += PRICE_TREE_SKIRT + PRICE_TREE_LIGHTS + PRICE_GARLANDS
    if days_count % 10 == 0 and days_count == days:
        christmas_spirit -= 30
    days_count += 1
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")

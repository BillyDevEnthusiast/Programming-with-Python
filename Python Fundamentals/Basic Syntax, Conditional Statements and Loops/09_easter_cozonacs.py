budget = float(input())
price_flour = float(input())

cozonak = 0
coloured_eggs = 0

price_egg = 0.75 * price_flour
price_milk = (price_flour * 1.25) / 4

price_cozonak = price_flour + price_egg + price_milk

while budget >= price_cozonak:
    cozonak += 1
    coloured_eggs += 3
    if cozonak % 3 == 0:
        coloured_eggs -= cozonak - 2
    budget -= price_cozonak
print(f"You made {cozonak} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")

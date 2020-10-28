items_list = input()
items = {}
while items_list != "buy":
    tokens = items_list.split()
    product = tokens[0]
    price = float(tokens[1])
    quantity = int(tokens[2])
    total_price = quantity * price

    if product not in items:
        items[product] = {}
        items[product]["price"] = price
        items[product]["quantity"] = quantity
        items[product]["total_price"] = total_price
        items_list = input()
        continue

    items[product]["quantity"] += quantity
    items[product]["total_price"] = items[product]["quantity"] * price

    items_list = input()

for i in items:
    print(f"{i} -> {items[i]['total_price']:.2f}")

def calculate_price(stuff, number):
    if product == "water":
        price = 1.00
    elif product == "coffee":
        price = 1.5
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2.0
    return price * number


product = input()
quantity = int(input())
print(f"{calculate_price(product, quantity):.2f}")

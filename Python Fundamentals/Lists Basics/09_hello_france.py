collection_of_items = input()
budget = float(input())
bought_products = []
new_prices = []

for item in collection_of_items.split('|'):
    tokens = item.split('->')
    type_of_product = tokens[0]
    product_price = float(tokens[1])
    if type_of_product == 'Clothes' and product_price > 50.0:
        continue
    if type_of_product == 'Shoes' and product_price > 35.0:
        continue
    if type_of_product == 'Accessories' and product_price > 20.5:
        continue

    if budget > product_price:
        budget -= product_price
        bought_products.append(product_price)
        new_prices.append(product_price * 1.4)


for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print('')

profit = sum(new_prices) - sum(bought_products)
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(new_prices)
if new_budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')

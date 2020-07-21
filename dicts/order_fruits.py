import time
from prettytable import PrettyTable

PRICE = 20

discounts = {
  'apple': 0.1,
  'banana': 0.15
}

fruits = [
  'apple',
  'banana',
  'orange',
  'apple',
  'banana',
  'apple',
  'orange',
  'apple',
  'orange',
  'graphe'
]

print('Step 1: Aggregate fruits cart')
cart = { fruit: fruits.count(fruit) * PRICE for fruit in fruits }
print(f'Cart aggregated: {cart}\n')
time.sleep(1)

print('Step 2: Apply discount')
for fruit in cart.keys():
    if fruit in discounts:
        cart[fruit] = cart[fruit] - ( cart[fruit] * discounts[fruit] )
print('Discount applied \n')
time.sleep(1)

print('Step 3: Calculate total price')
total_price = 0

for price in cart.values():
    total_price += price
time.sleep(1)
print(f'Total price: {total_price}\n')


print('Step 4: Provide finally bill')
table = PrettyTable()
table.title = 'Finally bill'
table.field_names = ['Fruit', 'Price ($)']

for fruit,price in cart.items():
    table.add_row([fruit, price])

table.add_row(['', ''])
table.add_row(['Total', total_price])
time.sleep(1)

print(table)


grocery_inventory = {
    'Milk': ('Dairy', 3.50, 8),
    'Eggs': ('Dairy', 5.50, 30),
    'Bread': ('Bakery', 2.99, 15),
    'Apples': ('Produce', 1.50, 50)
}

# Task 2: Check Eggs price and reduce if needed
egg_price = grocery_inventory['Eggs'][1]
if egg_price > 5:
    print('Eggs are too expensive, reducing the price by $1.')
    grocery_inventory['Eggs'] = (
        grocery_inventory['Eggs'][0],
        egg_price - 1,
        grocery_inventory['Eggs'][2]
    )
else:
    print('The price of Eggs is reasonable.')

# Task 3: Add Tomatoes
grocery_inventory.update({'Tomatoes': ('Produce', 1.20, 30)})
print('Inventory after adding Tomatoes:', grocery_inventory)

# Task 4: Manage Milk stock
milk_stock = grocery_inventory['Milk'][2]
if milk_stock < 10:
    old_cat, old_price, old_stock = grocery_inventory['Milk']
    grocery_inventory['Milk'] = (old_cat, old_price, old_stock + 20)
    print('Milk needs to be restocked. Increasing stock by 20 units.')
else:
    print('Milk has sufficient stock.')

# Task 5: Remove Apples if price > 2
apples_price = grocery_inventory['Apples'][1]
if apples_price > 2:
    grocery_inventory.pop('Apples', None)
    print('Apples removed from inventory due to high price.')

# Final print
print('Updated inventory:', grocery_inventory)
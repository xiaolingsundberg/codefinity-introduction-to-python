produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce,dairy]

for i in range(len(groceries)):
    
    for item in groceries[i]:
        print(f'Item name: - {item}')

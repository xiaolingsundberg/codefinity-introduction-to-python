# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Count how many times "apples" appear in the shelf tuple. 
# Store this in apple_count and print: "Number of Apples: <apple_count>".
apple_count = shelf.count('apples')
print('Number of Apples:', apple_count)


# Find the index of the first occurrence of "bananas" in the shelf tuple. 
# Store the index in banana_index and print: "First Banana Index: <banana_index>".
banana_index = shelf.index('bananas')
print('First Banana Index:', banana_index)


# Check if the number of apples is less than 5. 
# If true, print: "Apples need to be restocked." 
# Otherwise, print: "Apples are sufficiently stocked."
if apple_count < 5:
    print('Apples need to be restocked.')
else: 
    print('Apples are sufficiently stocked.')

# Count how many times "grapes" appear in the shelf tuple. 
# If grapes appear only once, print: "Grapes need to be restocked." 
# Otherwise, print: "Grapes are sufficiently stocked."
grapes_account = shelf.count('grapes')
if grapes_account == 1:
    print('Grapes need to be restocked.')
else:
    print('Grapes are sufficiently stocked.')


# Check if "oranges" exist in the shelf tuple. 
# If they do, print their index with: "Oranges are at index: <orange_index>". 
# If they don't exist, print: "Oranges are out of stock."
orange_index = shelf.index('oranges')

if 'oranges' in shelf:
    print('Oranges are at index:', orange_index)
else:
    print('Oranges are out of stock')


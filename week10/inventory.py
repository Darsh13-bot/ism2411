# Inventory.py
# Darsheel Panchal 
# Module 10 Lab: Inventory List Manager

#Reflection
#1. The most surprising thing about lists is that you can
# change them after creating them, using things like append(), remove(),
# and sort(). I also did not expect negative indexes like [-1] to work,
# since that gets the last item without needing to know the list's length.
#2. In a class project, I had to total and average a column
# of sales numbers, and in Excel I had to rewrite the formulas every time
# the data changed. With a Python list, I could loop through the numbers once
# and calculate the total, average, and highest sale automatically, and
# reuse the same code for any new data.

print("--- Excercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Excercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("--- Excercise 3: Slicing Practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2]) # every second item in the list

print("--- Excercise 4: Modifying the list ---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Excercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coodiantes: a location should not change by accident.")

print(coords)

print("--- Excercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Excercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted=[]
for price in prices:
    discounted.append(round(price * .9, 2))
    
print("Original prices:", prices)
print("Discounts:", discounted)

print("--- Excericse 8: Filter above a threshold")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
        
print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")

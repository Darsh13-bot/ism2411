# Darsheel Panchal Lab 6 excercises
# 09/30/2026
#Self-assessment questions:
#1. Set a starting value before the loop, and then update it with each item inside the loop, then use the final results when it ends. If you skip any part it would cause an error or partial answer. 
#2. The while loop version needed extra lines for the index, and the condition so it was longer and a little harder to accomplish compared to the for loop, which was much shorter and easier for lists. 
#3. At a random coffee shop for instnace, the list would hold tip amounts from each transaction in a shift. I would accumulate the total tips and count of the transactions made, and create a total and average tip per transaction. 

# Excercise 1
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Excercise 2 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# Excercise 3 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

# Excercise 4 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# Excercise 5 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale <= 100:
        continue          
    if sale > 400:
        print(f"Alert: outlier found ${sale}. Stopping.")
        break            
    print(f"${sale}")

# Excercise 6 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total: ${total}")
# In this, I would rather use the loop version instead, because it is more shorter and easier to understand, it doesnt need an index, and is easier to manage in general. 

# Excercise 7 
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale >= 200:
        rate = 10
    elif sale >= 100:
        rate = 5
    else:
        rate = 0
    discounted = sale * (1 - rate / 100)
    print(f"${sale} -> {rate}% discount -> ${discounted:.2f}")
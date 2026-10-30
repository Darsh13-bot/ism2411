# Self-assessment questions 
# 1. The first bug I spotted was the missing colon, which I found from the error message, since Python finds syntax errors more easier. The total = sale bug had no error, so I only caught it by noticing $90 didn’t match the expected $715, which tells me I rely on tracebacks, so I also need to look at tracing it as well. 
# 2. The (apply_discount(price, tier) takes a price and a tier name (“gold”, “silver”, “bronze”, or anything else) and returns the price after taking off 15%, 10%, 5%, or 0%. A colleague could use it without reading the body because the name, inputs, and return value make its purpose clear and easy to understand. 
# 3. Ai helped me built my understanding about the error explanations and how to fix them and debug. 
# AI-dosclosure: I used Claude (Excercise 5) to help me identify and explain the bugs in the broken_sales.py file. I also used it to help me understand the errors in the code and how to fix them. I did not use it to write any of the code or to complete any of the exercises

# --- Excercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# --- Excercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
    
# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")
    
# --- Excercise 3 ---

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Excercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


# --- Excercise 6 ---

x = 100 # apple #Global

def double_it():
    global x
    x = 999 # localanother apple (not the same apple as above)
    return x * 2

print(x)
print(double_it())
print(x)

# --- Excercise 5 ---
# 1. I think there might be a syntax error because in the for loop, there was no semicolon added after the end of the for statement, and there may be other syntax or logic errors. 
# 2. When I plugged in the code into Claude and asked it to explain to me the errors, it said "The first bug is that total = sale replaces the total on every loop instead of adding to it, so you end up with just the last sale ($90) instead of $715. The second bug is that the for sale in sales line is missing a colon at the end, which Python requires for loops. The third bug is that while i <= len(sales) lets i reach 5, but a 5-item list only has positions 0 through 4, so it crashes with an IndexError".
# 3. Inside the code
# 4. I found three bugs, the first being a logic bug where total = sale overwrote the total instead of adding to it, a syntax bug where the for line was missing a colon, and a runtime bug where <= when it should have been < and caused an index error. The AI’s explanations of the two error messages matched the real bugs well. 

# broken_sales.py - fixed 
sales = [120, 80, 250, 175, 90]
# Fix 1: total = sale replaces the total each time. Use += so each sale is added to it.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
# Fix 2: the for line is missing a colon. Add : at the end of the line.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
# Fix 3: i <= len(sales) lets i reach 5, which is out of its range. Use < so i stops exactlyat 4.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
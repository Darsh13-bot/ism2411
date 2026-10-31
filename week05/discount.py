# Lab 5: discount.py
# Self-assessment questions:
#1. The script checks the if/elif chain top to bottom, applying the first condition that's true. Since 350 is not ≥ 500, it skips the 15% tier. It checks ≥ 200 next, 350 qualifies, so discount is set to 10%, and Python stops checking further conditions. Final price = 350 × (1 - 0.10) = $315.00. Then that final price gets checked against the $1000 approval threshold, so since $315 is well under $1000, status = "auto_approved"
#2. "and" requires both conditions true in one combined check. Two separate if statements run independently a value like 50 or 600  would trigger each block differently than the " and"version. They're not equivalent unless you nest or coordinate them.
#3. Tiered conditional logic shows up in tax brackets, shipping fee thresholds or insurance premiums. Knowing how if elif else actually works makes you notice whether boundaries are inclusive or exclusive, whether tiers are marginal so only the amount within a range gets that rate or is included in that list. 
# Excercise 1:

total = float(input("Enter cart total: $"))

# Add if-elif-else

if total >= 500:
    discount = 0.15
elif total >=200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0

final = total * (1-discount)
print(f"Discount: {discount:.1%}") 
print(f"Final price: ${final:,.2f}")

# Excercise 3

region = "South"
extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.2
    print("Region bonus applied: additional 2% off")

final_discount = discount + extra_discount 
final = total * (1-final_discount) # Created here 

# Excercise 2

if final > 1000:
    status = "manager_approval_required" 
else:
    status = "auto_approed"

print(f"Status: {status}")

# Excercsie 4

customer_type = "wholesale"
# if region == "South":
#    if total > 100:
#        if customer_type == "wholesale":
#           estra_discount = 0.03

if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# Excercise 5

amount = -50

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE - REVIEW REQUIRED")

# Excercise 6

total_spent_this_year = 2500 
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_order = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_order) and not has_outstanding_balance

print(f"VIP upgrade: {vip_upgrade}")

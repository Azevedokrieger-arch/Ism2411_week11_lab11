from ast import For


print("--- exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["ytd_spend"])
print(customer["tier"])
print(customer)


print("--- exercise 2 ---")

customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))

print("--- exercise 3 ---")

#new version
print(customer.get("email", "no email on file"))

# #older version 
# try:
#     print(customer["email"])
# except KeyError:
#     print("KeyError Caught: {error}")


print("--- exercise 4 ---")
for key,value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

print("--- exercise 5 ---")
tier_discounts = {"bronze": 0, 
                  "silver": 0.5, 
                  "gold": 0.10, 
                  "platinum": 0.15}
purchase = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

print("--- exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in customers: 
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate # assuming a purchase amount of 300
    print(f"{record['name']} ({record['tier']}):  ${discount:.2f} discount on $300 purchase")

print("--- exercise 7 ---")
catalog = {
    "Widget A": { "price": 9.99, "stock": 150 },
    "Gadget C": { "price": 49.99, "stock": 8 }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock")

print("--- exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "East", "amount": 200},
]
sales_by_region = {} # empty dictionary to hold sales totals by region 
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print("sales_by_region:")

for region in sorted(sales_by_region.keys()):
    print(f"{region}: ${sales_by_region[region]:.2f}")

#In Exercise 3 you saw the difference between .get() and bracket notation. 
# When in real work would you use each one, and what's your rule of thumb for choosing?
# I would use .get() when a key might be missing and I need a default value, while bracket notation is appropriate when the key should exist and a missing key should raise an error.

#Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, 
# and why might the Python version be more useful for large datasets?
# This pattern is similar to Excel's SUMIF or PivotTable functionality, but Python can process large datasets more efficiently and flexibly, especially when the data structure is complex or when custom aggregation logic is needed.
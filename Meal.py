child_meal = float(input("What is the price of the child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

child_cost = child_meal * children
adult_cost = adult_meal * adults
subtotal = child_cost + adult_cost
print(f"Subtotal: ${subtotal:.2f}") 

sale_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (sale_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")

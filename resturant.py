# Restaurant Project - Updated Version
Menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

print('🍴 Welcome to Python Restaurant 🍴')
print("Here's our menu:")
for item, price in Menu.items():
    print(f"{item}: Rs {price}")

order_total = 0
order_summary = []

while True:
    item = input('\nEnter the item you want to order: ').title()
    if item in Menu:
        quantity = input(f"How many {item}s would you like? ")
        if quantity.isdigit():
            quantity = int(quantity)
            cost = Menu[item] * quantity
            order_total += cost
            order_summary.append(f"{item} x{quantity} = Rs {cost}")
            print(f"Added {quantity} {item}(s) to your order")
        else:
            print("Please enter a valid number for quantity!")
    else:
        print(f"Sorry, {item} is not available on the menu.")

    more = input("Do you want to order another item? (yes/no) ").lower()
    if more != 'yes':
        break

print("\n--- Your Order Summary ---")
for summary in order_summary:
    print(summary)
print(f"\nTotal amount to pay: Rs {order_total}")
print("Thank you for dining with us! 🍽️")

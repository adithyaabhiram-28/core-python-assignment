def calculate_total(cart_items):
    if not cart_items:
        return 0
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total -= total * 0.1
    return total

n = int(input("Enter number of items in cart: "))
cart_items = {}
for _ in range(n):
    item_name = input("Enter item name: ").strip()
    try:
        item_price = float(input("Enter item price: "))
        if item_price < 0:
            print("Invalid price, skipping item.")
            continue
        cart_items[item_name] = item_price
    except ValueError:
        print("Invalid input, skipping item.")

total_price = calculate_total(cart_items)
if total_price == 0:
    print("Cart is empty.")
else:
    print("Total Price:", int(total_price))

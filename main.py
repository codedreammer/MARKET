# Define the shops
fruits = {'name': 'fruits shop', 'orange': 70, 'banana': 20, 'grapes': 100, 'red berry': 50, 'mango': 35, 'apple': 70}
grocery = {'name': 'grocery shop', 'vegetable': 40, 'noodles': 30, 'washing detergent': 50, 'kitchen metrials': 75, 'junck fruits': 50}
Brijwasi_express = {'name': 'Brijwasi_express', 'sweets': 100, 'chat': 35, 'bakery products': 40}
salon = {'name': 'boys salon', 'hair-cut & beard': 80, 'massages': 70, 'waxing': 40, 'facial': 50}

shops = [fruits, grocery, Brijwasi_express, salon]

# Player's gold
gold = 1000

# Create an empty shopping cart
cart = {}

# Function to display items in a shop
def display_items(shop):
    print(f"Welcome to {shop['name']}!")
    for item, price in shop.items():
        if item != 'name':
            print(f"{item}: {price} gold")

# Function to buy an item
def buy_item(shop, item, gold):
    if item in shop:
        if gold >= shop[item]:
            gold -= shop[item]
            print(f"Bought {item} for {shop[item]} gold.")
            cart[item] = shop.pop(item)
        else:
            print("Not enough gold.")
    else:
        print("Item not available.")
    return gold

# Function to generate the bill
def generate_bill(cart):
    print("\n--- Bill ---")
    total_cost = 0
    for item, price in cart.items():
        print(f"{item}: {price} gold")
        total_cost += price
    print(f"Total cost: {total_cost} gold")
    print("Thank you for shopping with us!")


# Main game loop
def main():
    global gold
    for shop in shops:
        display_items(shop)
        while True:
            action = input("Enter item to buy or 'exit' to leave: ").lower()
            if action == 'exit':
                break
            gold = buy_item(shop, action, gold)
        print(f"Gold remaining: {gold}")
    
    print(f"\nYou purchased: {', '.join(cart.keys())}.")
    generate_bill(cart)
    

if __name__ == "__main__":
    main()

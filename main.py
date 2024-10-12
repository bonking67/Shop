# By Lucas Liu

# We want to simulate the process of a customer purchasing items from your store (the merchant) 
# We want them to be able to purchase multiple items, calculate the total cost (including any discounts), and get an itemized receipt
# In this project: input, dictionaries, lists, loops, conditionals (if statements)

# 1. Set up "inventory" data. Each item should have the following keys: Name, Stock, Price
# Create a dictionary for the first item containing the keys "name", "stock", "price". Assign values to each key
# Create two more additional item types

item1 = {"Name": "Book", "Stock": 3, "Price": 15.00}
item2 = {"Name": "Shirt", "Stock": 25, "Price": 35.00}
item3 = {"Name": "Mug", "Stock": 46, "Price": 8.00}

# 2. Create a list called "inventory" and add each item type that you created to the list.
# nums = [1, 2, 3]
# inventory = [item1, item2, item3]

inventory = []
inventory.append(item1)
inventory.append(item2)
inventory.append(item3)


# 3. Using a loop, print out each item in this format:
# "Item: NAME - $PRICE (STOCK left)"
# "Item: Book - $15.0 (3 left)"

def display_inventory():
    for item in inventory:
        # Correct: One string: "Hello {}".format()
        # Not correct: using multiple strings: "Hello {}" "x" "r".format()
        description = "{}  -  ${} ({} left)".format(item["Name"], item["Price"], item["Stock"])
        print(description)
print("\n")

# Hint: How to print out the price of item1 (print out the value of item1)
# item1["Price"]

# 4. Set up the customer experience.
# a. Write one message welcoming them to the store
# b. Write another message telling them what the inventory looks like.
  # Wrap step 3. inside a function so that we can reuse the code for displaying the inventory
  # Then, call the function to display the inventory

print("Hello. Welcome to Costco.")
display_inventory()
print("\n")


# Hint
# Define a function called "add" to add two numbers and return the sum
def add(num1, num2):
    return num1 + num2

    # result = num1 + num2
    # return result

# 5. Allow the customer to add something to their cart
# a. Allow them to select an item. If the item doesn't exist, give them a message and let them try again
# b. If the item does exist, allow them to select a quantity of the item
# c. If the item does not have enough quantity, give them a message and let them rechoose the quantity


total = 0
cart = {}

# Given the name of an item, retrieve its full data from the inventory
def find_item(customer_item):
    for item in inventory:
        if item["Name"] == customer_item:
            return item
    return False

print('If you are finished shopping, type "Im done." or "Im finished." to exit.')
while True:
    customer_item = input("What are you looking for today? ")
    if customer_item == "Im done." or customer_item == "Im finished.":
        break
    searched_item = find_item(customer_item)
    if searched_item != False:
        customer_item_count = int(input("How many of these do you want? "))
        if searched_item["Stock"] >= customer_item_count:
            searched_item["Stock"] -= customer_item_count
            total += searched_item["Price"] * customer_item_count
            cart[searched_item["Name"]] = customer_item_count
            print("{} {}s has been added to cart.".format(customer_item_count,searched_item["Name"].lower()))
            print("Cart: {}".format(cart))
            print("Total: ${}0".format(total))
        elif searched_item["Stock"] == 0:
            print("Sorry, we do not have that anymore of that item in stock.")
        else:
            print("Sorry, we do not have your requested amount of {}s in stock. {}: {} left".format(searched_item["Name"].lower(), searched_item["Name"], searched_item["Stock"]))
    else:
        print("Sorry we do not have that item.")


tax = total*9.63/100
print("\n")
print("Thank you for shopping with us.")
print("\n")


for bought_item in cart:
    item = find_item(bought_item)
    price_of_item = item["Price"]
    print("{}: {} - ${:.2f}".format(bought_item, cart[bought_item], cart[bought_item] * price_of_item))


print("\n")
print("Cost: ${:.2f} ".format(total))
print("Tax: ${:.2f}".format(tax))
total = total + tax
print("Total: ${:.2f}".format(total))





# Hint
# first_name = input("What is your first name?")






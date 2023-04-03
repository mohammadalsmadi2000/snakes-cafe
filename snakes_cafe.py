

# store user orders
order = {}

# Define the menu
menu = {
    "appetizers": ["Wings", "Cookies", "Spring Rolls"],
    "entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
    "desserts": ["Ice Cream", "Cake", "Pie"],
    "drinks": ["Coffee", "Tea", "Unicorn Tears"]
}


# print the menu
def print_menu():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type 'quit' **")
    print("**************************************")
    for section, items in menu.items():# section key=(appetizers,entrees,desserts,desserts,drinks) items pair
        print("\n" + section.capitalize()) #capitalize(): converts the first character of a string to an uppercase letter and all other alphabets to lowercase
        print("-" * len(section))# To add (-) according to the number of letters of the key
        for item in items: # print item from each itmes
            print(item)
    print("\n" + "*" * 35)
    print("** What would you like to order? **")
    print("*" * 35)



# print the order
def print_order(order):
    print("\n" + "=" * 25)
    print("     YOUR ORDER SUMMARY")
    print("=" * 25 + "\n")
    for item, count in order.items():
        print(f"{count} order(s) of {item} have been added to your meal")
    print("=" * 25 + "\n")



# program start from here
while True:
    print_menu()# print menu
    user_input = input("> ").capitalize()
    if user_input == "quit":# Allows the user to exit at any time they enter quit
        break
    else:
        found_inside_menu = False 
        for section, items in menu.items():
            if user_input in items:
                order[user_input] = order.get(user_input, 0) + 1
                print(f"\n** {order[user_input]} order(s) of {user_input} have been added to your meal **\n")
                found_inside_menu = True
                break
        if not found_inside_menu:
            print("Sorry, we don't have that item on the menu... Please try again.")



# Print the order summary when the user exits
print_order(order) 

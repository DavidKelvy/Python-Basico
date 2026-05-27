requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Desculpe, estamos sem pimentões verdes no momento.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
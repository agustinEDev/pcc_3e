def make_pizza (size, *toppings):
    print(f"Making a {size} size pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}.")

make_pizza(12, 'tomate', 'mozzarella', 'peperonni', 'bacon')
make_pizza(16, 'cheese')
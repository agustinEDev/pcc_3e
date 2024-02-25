from modulos.name_function import get_formated_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease, enter a first name: ")
    if first == 'q':
        break
    last = input("Please, enter a las name: ")
    if last == 'q':
        break

    formated_name = get_formated_name(first, last)
    print(f"Neatly formatted name: {formated_name}.")
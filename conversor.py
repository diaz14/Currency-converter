menu = input("""
Welcome to Mexico! Please, select a desired convertion 💰

USD currency ($) == 1
EUR currency (€) == 2

""")
menu = int(menu)
if menu == 1:
    dollar = int(input("How many US dollars do you have?: "))
    mx_peso = 0.050
    us_value = dollar / mx_peso
    us_value = round(us_value, 2)
    us_value = str(us_value)
    print("Then, you've $" + us_value + " mexican pesos!")
elif menu == 2:
    euro = int(input("How many euro do you have?: "))
    mx_peso = 0.051
    eu_value = euro / mx_peso
    eu_value = round(eu_value, 2)
    eu_value = str(eu_value)
    print("Then, you've $" + eu_value + " mexican pesos!")
else:
    print("Invalid input. Please, select an option.")
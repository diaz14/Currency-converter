def converter(currency, peso_value):
    currency = float(input("How many " + currency + " do you have?: "))
    peso = currency / peso_value
    peso = round(peso, 2)
    peso = str(peso)
    print("You've $" + peso + " mexican pesos!")

menu = """
Welcome to Mexico! Please, select a desired convertion 💰

1 - USD currency ($)
2 - EUR currency (€)
3 - GBP currency (£)

▶ """

option = float(input(menu))

if option == 1:
    converter("USD dollars", 0.050)
elif option == 2:
    converter("EURO", 0.051)
elif option == 3:
    converter("british pounds", 0.044)
else:
    print("Invalid input. Please, select options 1, 2 or 3.")
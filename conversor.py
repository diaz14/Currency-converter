peso = input("¿Cuántos pesos mexicanos tienes?: ")
peso = float(peso)
valor_dolar = 19.97
valor_dolar = peso/valor_dolar
valor_dolar = round(valor_dolar, 2)
print str("Tienes $ " + valor_dolar + "dólares")
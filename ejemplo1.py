"""Un usuario introduce texto desde teclado y queremos
averiguar si es un número entero. Si es entero lo
añadiremos a una variable tipo lista de números
enteros. """
lista= list()
texto = input("introduzca un numero")
if texto.isnumeric():
    num = int(texto)
    lista.append(num)
    print(lista)
else:
    print("no es numerico")


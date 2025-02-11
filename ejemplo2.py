diccionario = {"247419292": 38,  "20325965": 40} # creando diccionario 
texto = input("introduzca un numero de documento")
if texto in diccionario:
 # Para imprimir el valor de un elemento de un diccionario en Python, puedes acceder al valor utilizando la clave asociada a ese valor.
    print ("la edad del ID: "+ texto + "es: " + str(diccionario[texto]))
else:
    if texto.isnumeric():
        num= int(texto)
        diccionario[texto] = num
        print("añadido al diccionario")
print(diccionario)

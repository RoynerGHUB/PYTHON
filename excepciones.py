def indexador(cadena, indice):
    #print(cadena[indice]) 
    try:
        return cadena[indice]
    
    except IndexError: 
        print("has colocado un indice muy grande")
    print("hemos salido del try-cacht")


print(indexador("royner", 10))
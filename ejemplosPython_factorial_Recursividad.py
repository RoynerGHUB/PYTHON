def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
resultado=factorial(5)
print(resultado)

def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función
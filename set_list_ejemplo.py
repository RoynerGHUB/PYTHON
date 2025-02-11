my_list = list()
my_set = set()

l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del Set: "))
a, b, c,d =map(int, input("Introduzca valores para las variables a, b, y d: ").split(','))
while True:
    valores =input("introduzca 3 valores").split(' ')
    print(valores)
    if len(valores) == 3:
        print("correto")
    else:
        print("incorrecto")
        break
print("Introduzca los elementos de la lista: ")
for i in range(l):
    num= int(input(f"ingrese el elemento {i}: "))
    my_list.append(int(num))
    #crear y llenar una tupla de la lista creada en el paso anterior
    tupla = tuple(my_list)
print("Introduzca los elementos del Set: ")
for i in range(s):
    nums = int(input(f"Ingrese los elementos del set {i}: "))
    my_set.add(int(nums))

print(my_list)
print(my_set)
print(tupla, type(tupla))
print(a,b,c,d)
print("el valor de a {} y b {}".format(a,b))
class Vehiculo():
  
    def  __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'color: '+ self.color + ', ruedas:' + str(self.ruedas)
    
class Coche(Vehiculo):
    def  __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return 'color: '+ self.color + ', ruedas:' + str(self.ruedas) + ' Velocidad, ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
            super().__init__(color, ruedas)
            self.tipo = tipo

    def __str__(self):
         return super().__str__()+' ' +'Tipo: '+  self.tipo

miCoche = Coche("rojo", 4, 100 )
print(miCoche)

miBicicleta= Bicicleta("verde",2,"Montaña")
print(miBicicleta)

miVehiculo = Vehiculo("amarillo",4)
print(miVehiculo)
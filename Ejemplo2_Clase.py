class Empleado():
    def __init__(self, nombre,cedula, telefono):
        self._nombre= nombre
        self._cedula = cedula
        self._telefono = telefono
       

    def set_nombre(self,nombre):
        self._nombre = nombre
 
    def get_nombre(self):
        return self._nombre
    
    def set_cedula(self, cedula):
        self._set_cedula = cedula

    def get_cedula(self):
        return self._cedula
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
    
class empleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono,nplaza, salarioBase,duracion_contrato):
        super().__init__(nombre, cedula, telefono)
        self._nplaza = nplaza
        self._salarioBase= salarioBase
        self._duracion_contrato = duracion_contrato


    def set_nplaza(self, nplaza):
        self._nplaza= nplaza

    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase

    def set_duracion_contrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato

    def get_nplazas(self):
        return self._nplaza
    
    def get_salarioBase(self):
        return self._salarioBase
    
    def get_duracion_contrato(self):
        self._duracion_contrato


    def aumentoSalario(self):
       return (self._salarioBase * 100/2) + self.salarioBase
    
class empleadoIndefinido(Empleado):
    def __init__(self, nombre, cedula, telefono,nplaza,salarioBase,categoria):
        super().__init__(self, nombre, cedula, telefono) 
        self._nplaza= nplaza
        self._salarioBase=salarioBase
        self._categoria= categoria

    def set_nplaza(self, nplaza):
        self._nplaza = nplaza

    def get_nplaza(self):
        return self._nplaza


    def set_salarioBase(self, salarioBase):
        self._salarioBase = salarioBase

    def get_salarioBase(self):
        return self._salarioBase
    
    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria

    def calcularSalario(self):
        if self._categoria ==1:
            return self._salarioBase+(self._salarioBase * 3/100) 
        elif self._categoria ==2:
           return self._salarioBase+(self._salarioBase * 5/100)
        elif self._categoria ==3:
            return self._salarioBase+(self._salarioBase * 8/100)
        else:
         return self._salarioBase
        
class subContratado(Empleado):
    def __init__(self, nombre, cedula, telefono, empresa_responsable):
        super().__init__(nombre, cedula, telefono) 
        self._empresa_responsable = empresa_responsable

    def set_empresa_responsable(self, empresa_responsable):
        self._empresa_responsable= empresa_responsable

    def get_empresa_responsable(self):
        return self._empresa_responsable 
    

    '''ejecucion del codigo'''

subContratado1 = subContratado("Roberto Flores Morales", 123456789, 88888888,
"Coca-Cola")
print("*********Empleados SubContratados********")
print("el nombre del empleado: " + subContratado1.get_nombre() +
      "\n con Cedula :" + str(subContratado1.get_cedula()))



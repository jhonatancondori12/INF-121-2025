class Clima:
    def __init__(self, tipo, temperatura, precipitacion):
        self._tipo = tipo
        self._temperatura = temperatura
        self._precipitacion = precipitacion
        
    def get_tipo(self):
        return self._tipo
    
    def get_temperatura(self):
        return self._temperatura
    
    def get_precipitacion(self):
        return self._precipitacion
    
    def set_tipo(self, tipo):
        self._tipo = tipo
    
    def set_temperatura(self, temperatura):
        self._temperatura = temperatura
    
    def set_precipitacion(self, precipitacion):
        self._precipitacion = precipitacion

    def describir_clima(self):
        print(f"Clima {self._tipo}: {self._temperatura}°C y {self._precipitacion} mm de lluvia.")
        
    def comparar_temperatura(self, otro_clima):
        if self._temperatura > otro_clima.get_temperatura():
            print(f"El clima {self._tipo} es más cálido que el clima {otro_clima.get_tipo()}.")
        elif self._temperatura < otro_clima.get_temperatura():
            print(f"El clima {self._tipo} es más frío que el clima {otro_clima.get_tipo()}.")
        else:
            print(f"Ambos climas tienen la misma temperatura.")

class Planta:
    def __init__(self, nombre, semilla, adaptabilidad):
        self._nombre = nombre
        self._semilla = semilla
        self._adaptabilidad = adaptabilidad

    def get_nombre(self):
        return self._nombre
    
    def get_semilla(self):
        return self._semilla
    
    def get_adaptabilidad(self):
        return self._adaptabilidad

    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_semilla(self, semilla):
        self._semilla = semilla
    
    def set_adaptabilidad(self, adaptabilidad):
        self._adaptabilidad = adaptabilidad

    def expandir(self, clima):
        if clima.get_temperatura() >= 20 and clima.get_precipitacion() >= 100:
            print(f"La planta {self._nombre} puede expandirse en este clima.")
        else:
            print(f"La planta {self._nombre} no se expande por condiciones climáticas.")
    
    def florecer(self):
        print(f"La planta {self._nombre} está en fase de floración.")

class Geografia:
    def __init__(self, tipo, barreras):
        self._tipo = tipo
        self._barreras = barreras

    def get_tipo(self):
        return self._tipo
    
    def get_barreras(self):
        return self._barreras

    def set_tipo(self, tipo):
        self._tipo = tipo
    
    def set_barreras(self, barreras):
        self._barreras = barreras

    def mostrar_barreras(self):
        print(f"En la geografía {self._tipo} existen barreras como: {', '.join(self._barreras)}.")
    
    def comparar_geografia(self, otra_geografia):
        if self._tipo == otra_geografia.get_tipo():
            print(f"Ambas geografías son del mismo tipo: {self._tipo}.")
        else:
            print(f"Las geografías son diferentes: {self._tipo} vs {otra_geografia.get_tipo()}.")

clima1 = Clima("Tropical", 28, 150)
clima2 = Clima("Desértico", 40, 30)
planta1 = Planta("Quinua", "semilla pequeña", "alta")
geo1 = Geografia("Montañosa", ["cordilleras", "ríos", "pendientes empinadas"])
geo2 = Geografia("Llanura", ["valles", "planicies"])

clima1.describir_clima()
clima1.comparar_temperatura(clima2)

planta1.set_nombre("Arroz")
print(planta1.get_nombre())

geo1.set_barreras(["desiertos", "canyon", "volcanes"])
geo1.mostrar_barreras()

planta1.expandir(clima1)
planta1.florecer()

geo1.mostrar_barreras()
geo1.comparar_geografia(geo2)

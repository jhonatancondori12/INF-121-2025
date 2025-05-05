class Gobierno:
    def __init__(self, nombre, region, acciones, responsable):
        self._nombre = nombre
        self._region = region
        self._acciones = acciones
        self._responsable = responsable

    def nombre(self):
        return self._nombre

    def nombre(self, valor):
        self._nombre = valor

    def region(self):
        return self._region

    def region(self, valor):
        self._region = valor

    def acciones(self):
        return self._acciones

    def acciones(self, valor):
        self._acciones = valor

    def responsable(self):
        return self._responsable

    def responsable(self, valor):
        self._responsable = valor

    def mostrar_inaccion(self):
        return f"1. El gobierno {self._nombre} no tomó acciones claras en {self._region}."

    def tomar_accion(self, nueva_accion):
        self._acciones.append(nueva_accion)
        return f"Acción '{nueva_accion}' agregada al plan del gobierno."

class ComunidadIndigena:
    def __init__(self, nombre, contaminantes, regiones, lider):
        self._nombre = nombre
        self._contaminantes = contaminantes
        self._regiones = regiones
        self._lider = lider

    def nombre(self):
        return self._nombre

    def nombre(self, valor):
        self._nombre = valor

    def contaminantes(self):
        return self._contaminantes

    def contaminantes(self, valor):
        self._contaminantes = valor

    def regiones(self):
        return self._regiones

    def regiones(self, valor):
        self._regiones = valor

    def lider(self):
        return self._lider

    def lider(self, valor):
        self._lider = valor

    def denunciar(self):
        return f"2. La comunidad {self._nombre} denuncia contaminación por {', '.join(self._contaminantes)} en {', '.join(self._regiones)}."

    def agregar_contaminante(self, contaminante):
        self._contaminantes.append(contaminante)
        return f"Contaminante '{contaminante}' agregado."

class EmpresaMinera:
    def __init__(self, nombre, minerales, compensacion, ubicacion):
        self._nombre = nombre
        self._minerales = minerales
        self._compensacion = compensacion
        self._ubicacion = ubicacion

    def nombre(self):
        return self._nombre

    def nombre(self, valor):
        self._nombre = valor

    def minerales(self):
        return self._minerales

    def minerales(self, valor):
        self._minerales = valor

    def compensacion(self):
        return self._compensacion

    def compensacion(self, valor):
        self._compensacion = valor

    def ubicacion(self):
        return self._ubicacion

    def ubicacion(self, valor):
        self._ubicacion = valor

    def exigir_compensacion(self):
        if self._compensacion:
            return f"3. La empresa {self._nombre} debe compensar por la explotación de {', '.join(self._minerales)}."
        else:
            return f"La empresa {self._nombre} aún no ha establecido un fondo de compensación."

    def agregar_mineral(self, mineral):
        self._minerales.append(mineral)
        return f"Mineral '{mineral}' agregado a la lista de extracción."
#----salida:---
gob = Gobierno("Gobierno Nacional", "Amazonía", [], "Luis Arce")
print(gob.mostrar_inaccion())
print(gob.tomar_accion("Crear fondo de compensación"))

com = ComunidadIndigena("Uchupiamonas", ["mercurio", "plomo"], ["Madidi", "Pando"], "Lino Villuni")
print(com.denunciar())
print(com.agregar_contaminante("arsénico"))

emp = EmpresaMinera("Minera San José", ["oro", "estaño"], True, "Potosí")
print(emp.exigir_compensacion())
print(emp.agregar_mineral("plata"))

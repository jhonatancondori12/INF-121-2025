class Ministerio:
    def __init__(self, nombre, direccion, nombres, edades, sueldos):
        self.nombre = nombre
        self.direccion = direccion
        self.nombres = nombres
        self.edades = edades
        self.sueldos = sueldos

    def transferir_empleado(self, index_empleado, otro_ministerio):
        empleado = self.nombres.pop(index_empleado)
        edad = self.edades.pop(index_empleado)
        sueldo = self.sueldos.pop(index_empleado)

        otro_ministerio.nombres.append(empleado)
        otro_ministerio.edades.append(edad)
        otro_ministerio.sueldos.append(sueldo)

    def mostrar_empleado(self, criterio="mayor_edad"):
        if not self.nombres:
            print("No hay empleados.")
            return

        if criterio == "mayor_edad":
            idx = self.edades.index(max(self.edades))
            print(f"Mayor edad: {self.nombres[idx]}, {self.edades[idx]} años")

        elif criterio == "mayor_sueldo":
            idx = self.sueldos.index(max(self.sueldos))
            print(f"Mayor sueldo: {self.nombres[idx]}, Bs {self.sueldos[idx]}")

        elif criterio == "menor_edad":
            idx = self.edades.index(min(self.edades))
            print(f"Menor edad: {self.nombres[idx]}, {self.edades[idx]} años")

        elif criterio == "menor_sueldo":
            idx = self.sueldos.index(min(self.sueldos))
            print(f"Menor sueldo: {self.nombres[idx]}, Bs {self.sueldos[idx]}")

        else:
            print("Criterio no reconocido.")

# Crear ejemplo
ministerio = Ministerio(
    "Ministerio de Justicia",
    "Av. Bolívar",
    ["Juan", "Marta", "Pedro"],
    [34, 28, 45],
    [4200, 3900, 4700]
)

# Llamadas al método sobrecargado
ministerio.mostrar_empleado("menor_edad")
ministerio.mostrar_empleado("menor_sueldo")

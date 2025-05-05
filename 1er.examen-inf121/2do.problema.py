class LineaTeleferico:
    def __init__(self, color, tramo, direccion, nombres, edades, sueldos):
        self.color = color
        self.tramo = tramo
        self.direccion = direccion
        self.nombres = nombres
        self.edades = edades
        self.sueldos = sueldos
    
    def mostrar_empleado_mayor_edad(self):
        max_edad = max(self.edades)
        index = self.edades.index(max_edad)
        print(f"Empleado mayor edad: {self.nombres[index]} con {max_edad} años")
    
    def mostrar_empleado_mayor_sueldo(self):
        max_sueldo = max(self.sueldos)
        index = self.sueldos.index(max_sueldo)
        print(f"Empleado con mayor sueldo: {self.nombres[index]} gana {max_sueldo} Bs")

# Instanciación de dos objetos
teleferico1 = LineaTeleferico("Rojo", "Tramo1", "Estación Central", ["Pedro", "Ana", "Luisa", "Raul"], [35, 29, 43, 26], [2500, 2500, 3500, 2000])
teleferico2 = LineaTeleferico("Verde", "Tramo2", "Estación Cementerio", ["Sonia", "Luis", "Alex", "Sara"], [28, 33, 38, 29], [2400, 3000, 2800, 2700])

# Mostrar resultados
teleferico1.mostrar_empleado_mayor_edad()
teleferico1.mostrar_empleado_mayor_sueldo()

from abc import ABC, abstractmethod
import random
import tkinter as tk
from tkinter import ttk, messagebox

# Interfaz Colorado
class Colorado(ABC):
    @abstractmethod
    def como_colorear(self) -> str:
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return f"Color: {self.color}"

# Clase Cuadrado
class Cuadrado(Figura, Colorado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - {super().__str__()} - Lado: {self.lado}"

# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio

    def __str__(self):
        return f"Circulo - {super().__str__()} - Radio: {self.radio}"

# ------- Interfaz gráfica ------
def generar_figuras():
    lista_figuras = []
    salida.delete(0, tk.END)

    for _ in range(10):
        tipo = random.choice(["cuadrado", "circulo"])
        color = random.choice(["Rojo", "Verde", "Azul"])
        tamaño = random.randint(1, 10)

        if tipo == "cuadrado":
            figura = Cuadrado(tamaño, color)
        else:
            figura = Circulo(tamaño, color)

        lista_figuras.append(figura)

    for f in lista_figuras:
        desc = f"{f.__str__()}, Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}"
        if isinstance(f, Colorado):
            desc += f", {f.como_colorear()}"
        salida.insert(tk.END, desc)

# Ventana principal
ventana = tk.Tk()
ventana.title("Figuras Coloreadas")
ventana.geometry("600x400")

boton = ttk.Button(ventana, text="Generar Figuras", command=generar_figuras)
boton.pack(pady=10)

salida = tk.Listbox(ventana, width=90, height=15)
salida.pack(pady=10)

ventana.mainloop()

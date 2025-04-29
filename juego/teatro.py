import tkinter as tk
from tkinter import messagebox

class Boleto:
    def __init__(self, numero):
        self.numero = numero
    def obtener_precio(self):
        return 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.obtener_precio():.2f}"


class Palco(Boleto):
    def obtener_precio(self):
        return 100.0


class Platea(Boleto):
    def obtener_precio(self):
        return 60.0


class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion

    def obtener_precio(self):
        if self.dias_anticipacion >= 10:
            return 25.0
        else:
            return 30.0


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")

        # Título
        tk.Label(root, text="Teatro Municipal", font=("Arial", 16)).pack(pady=10)

        # Frame principal
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Tipo de boleto
        self.tipo_boleto = tk.StringVar()
        self.tipo_boleto.set("Palco")

        tk.Label(frame, text="Tipo de Boleto:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(frame, text="Palco", variable=self.tipo_boleto, value="Palco").grid(row=0, column=1)
        tk.Radiobutton(frame, text="Platea", variable=self.tipo_boleto, value="Platea").grid(row=0, column=2)
        tk.Radiobutton(frame, text="Galería", variable=self.tipo_boleto, value="Galeria").grid(row=0, column=3)

        # Número de boleto
        tk.Label(frame, text="Número:").grid(row=1, column=0, sticky="e")
        self.entry_numero = tk.Entry(frame)
        self.entry_numero.grid(row=1, column=1)

        # Días anticipación (solo útil para Galería)
        tk.Label(frame, text="Días antes del evento:").grid(row=2, column=0, sticky="e")
        self.entry_dias = tk.Entry(frame)
        self.entry_dias.grid(row=2, column=1)

        # Botones
        tk.Button(root, text="Ver Precio", command=self.mostrar_precio).pack(pady=5)
        self.lbl_resultado = tk.Label(root, text="Número: -, Precio: 0.0", font=("Arial", 12))
        self.lbl_resultado.pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack()

    def mostrar_precio(self):
        try:
            numero = int(self.entry_numero.get())
            tipo = self.tipo_boleto.get()

            if tipo == "Palco":
                boleto = Palco(numero)
            elif tipo == "Platea":
                boleto = Platea(numero)
            elif tipo == "Galeria":
                dias = int(self.entry_dias.get())
                boleto = Galeria(numero, dias)
            else:
                raise ValueError("Tipo de boleto no válido")

            self.lbl_resultado.config(text=str(boleto))

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos")


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()

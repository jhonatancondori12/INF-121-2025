import math

class FiguraGeometrica:
    def area_circulo(self, radio):
        return math.pi * radio * radio

    def area_rectangulo(self, base, altura):
        return base * altura

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2

    def area_hexagono(self, lados):
        return math.pi * (lados * lados)

if __name__ == "__main__":
    f = FiguraGeometrica()
    print("Círculo:", f.area_circulo(1))
    print("Rectángulo:", f.area_rectangulo(2, 3))
    print("Triángulo Rectángulo:", f.area_triangulo(5, 5))
    print("Trapecio:", f.area_trapecio(10, 6, 5))
    print("Hexágono:", f.area_hexagono(4))

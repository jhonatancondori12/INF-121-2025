package hola;

public class FiguraGeometrica {
	
	double area(double radio) {
		return Math.PI * radio * radio ; //circulo
	}
	
	double area(double base, double altura) {
		return base * altura ; //rectangulo
	}
	
	double area1(double base , double altura) {
		return (base * altura) /2 ; //triangulo rectangulo
	}
	
	double area(double baseMayor, double baseMenor , double altura ) {
		return ((baseMayor + baseMenor) * altura)/2 ; //trapecio
	}
	
	double area1(double lados) {
		return Math.PI * (lados * lados); //hexagono
	}
	public static void main(String[] args) {
		FiguraGeometrica f1 = new FiguraGeometrica();
		FiguraGeometrica f2 = new FiguraGeometrica();
		FiguraGeometrica f3 = new FiguraGeometrica();
		FiguraGeometrica f4 = new FiguraGeometrica();
		FiguraGeometrica f5 = new FiguraGeometrica();
		System.out.println("circulo: "+ f1.area(1));
		System.out.println("rectangulo: "+ f2.area(2,3));
		System.out.println("trianguloRectangulo: "+ f3.area(5,5));
		System.out.println("trapecio: "+ f4.area(10,6,5));
		System.out.println("hexagono: "+ f5.area(4));
	}

}

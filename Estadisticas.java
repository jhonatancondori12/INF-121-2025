package laboratorio1;

import java.util.Scanner;
import java.util.Locale; 

public class Estadisticas {
    private double[] numeros;

    public Estadisticas(double[] numeros) {
        this.numeros = numeros;
    }

    public double calcularPromedio() {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }

    public double calcularDesviacion() {
        double promedio = calcularPromedio();
        double sumaCuadrados = 0;
        for (double num : numeros) {
            sumaCuadrados += Math.pow(num - promedio, 2);
        }
        return Math.sqrt(sumaCuadrados / (numeros.length - 1));
    }

    public void mostrarResultados() {
        System.out.printf("El promedio es %.2f%n", calcularPromedio());
        System.out.printf("La desviación estándard es %.5f%n", calcularDesviacion());
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.US);

        double[] numeros = new double[10];

        System.out.println("Ingrese 10 números:");
        for (int i = 0; i < 10; i++) {
            numeros[i] = scanner.nextDouble();
        }

        Estadisticas estadisticas = new Estadisticas(numeros);
        estadisticas.mostrarResultados();

        scanner.close();
    }
}

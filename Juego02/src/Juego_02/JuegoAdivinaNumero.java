package Juego_02;

import java.util.Scanner;

public class JuegoAdivinaNumero {
    protected int vidas;

    public JuegoAdivinaNumero() {
        this.vidas = 3;
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega() {
        Scanner sc = new Scanner(System.in);
        int numeroSecreto = (int) (Math.random() * 11);
        System.out.println("Adivina el número (entre 0 y 10):");

        while (vidas > 0) {
            System.out.print("Introduce tu intento: ");
            int intento = sc.nextInt();

            if (!validaNumero(intento)) {
                System.out.println("Número no válido. Debe estar entre 0 y 10.");
                continue;
            }

            if (intento == numeroSecreto) {
                System.out.println("¡Adivinaste el número!");
                return;
            } else {
                vidas--;
                if (vidas == 0) {
                    System.out.println("Te has quedado sin vidas. El número secreto era " + numeroSecreto);
                } else {
                    System.out.println("Intenta de nuevo. Te quedan " + vidas + " vidas.");
                }
            }
        }
    }
}

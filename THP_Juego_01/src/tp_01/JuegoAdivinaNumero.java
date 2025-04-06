package tp_01;

import java.util.Scanner;
import java.util.Random;

public class JuegoAdivinaNumero extends Juego {
    private int numeroAAdivinar;

    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    public void juega() {
        reiniciaPartida();
        Random random = new Random();
        numeroAAdivinar = random.nextInt(11);
        System.out.println("🎮 Adivina un número entre 0 y 10:");
        Scanner scanner = new Scanner(System.in);
        int intentos = 0;

        while (true) {
            System.out.print("Tu número: ");

            if (!scanner.hasNextInt()) {
                System.out.println("Por favor, ingresa un número válido.");
                scanner.next();
                continue;
            }

            int intento = scanner.nextInt();
            intentos++;

            if (intento == numeroAAdivinar) {
                System.out.println("¡Acertaste en " + intentos + " intento(s)!");
                actualizaRecord(intentos);
                break;
            } else {
                if (!quitaVida()) {
                    System.out.println("¡No te quedan más vidas! El número era: " + numeroAAdivinar);
                    break;
                } else {
                    if (intento < numeroAAdivinar) {
                        System.out.println("El número es mayor. Vidas restantes: " + numeroDeVidas);
                    } else {
                        System.out.println("El número es menor. Vidas restantes: " + numeroDeVidas);
                    }
                }
            }
        }
    }
}

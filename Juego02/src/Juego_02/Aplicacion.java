package Juego_02;

public class Aplicacion {

    public static void main(String[] args) {
        JuegoAdivinaNumero juegoNumero = new JuegoAdivinaNumero();
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar();
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar();

        System.out.println("Juego Adivina Número:");
        juegoNumero.juega();

        System.out.println("\nJuego Adivina Par:");
        juegoPar.juega();

        System.out.println("\nJuego Adivina Impar:");
        juegoImpar.juega();
    }
}

package tp_01;

public class Juego { 
    protected int numeroDeVidas;
    protected int record;

    public Juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

    public void reiniciaPartida() {
        System.out.println("Reiniciando partida");
    }

    public void actualizaRecord(int intentos) {
        if (record == 0 || intentos < record) {
            record = intentos;
            System.out.println("¡Nuevo récord! Intentos: " + record);
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        System.out.println("Vidas restantes: " + numeroDeVidas);
        return numeroDeVidas > 0;
    }
}

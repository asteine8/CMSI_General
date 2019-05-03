import java.util.*;

class TetrisProgram extends TimerTask {
    public void run() {
        Tetris.display.run();
    }
}

public class Tetris {
    public static Display display;
    public static Timer timer;
    public static Random random;

    public static void main(String[] args) {
        timer = new Timer();
        random = new Random();
        display = new Display();

        // Start the program at 10HZ
        timer.scheduleAtFixedRate(new TetrisProgram(), 1000L, 200L);
    }

    public static void terminate() {
        timer.cancel();
        timer.purge();
        // exit();
    }
}
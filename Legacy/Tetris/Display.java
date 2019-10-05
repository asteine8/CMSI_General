import java.util.*;

public class Display {
    public static final int WIDTH = 10;
    public static final int HEIGHT = 16;

    private List<Pixel> pixels;
    private Scanner scanner;

    public Display() {
        this.scanner = new Scanner(System.in);
        this.pixels = new ArrayList<Pixel>();

        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                this.pixels.add(new Pixel(i, j));
            }
        }
        
        for (int i = 0; i < this.pixels.size(); i++) {
            this.pixels.get(i).symbol = Tetris.random.nextBoolean() ? " " : "*";
        }
    }

    public void run() {
       

        displayPixels();
    }

    public void renderBlocks(List<Block> blocks) {

    }

    private void displayPixels() {
        String output = "";
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                output += this.getPixel(i, j).symbol;
            }
            output += "\n";
        }
        System.out.println(output);
    }

    // Base 0 please
    public Pixel getPixel(int row, int col) {
        return this.pixels.get(row*WIDTH + col);
    }
}
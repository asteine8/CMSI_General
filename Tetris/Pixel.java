public class Pixel {
    public static final String DEFAULT_SYMBOL = " ";

    public int row;
    public int col;
    public String symbol;

    public Pixel() {
        this.row = 0;
        this.col = 0;
        this.symbol = DEFAULT_SYMBOL;
    }

    public Pixel(int row, int col) {
        this.row = row;
        this.col = col;
        this.symbol = DEFAULT_SYMBOL;
    }

    public boolean equals(Pixel p) {
        return p.symbol.equals(this.symbol);
    }

    public boolean equals(String str) {
        return str.equals(this.symbol);
    }
}
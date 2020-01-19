public class InplaceSwap {
    public static void main(String[] args) {
        int x = 42;
        int y = 64;
        // x, y
        // x ^ y, y
        // x ^ y, y ^ ~(x ^ y) = x
        // (x ^ y) ^ x = y, x
        x = x ^ y;
        y = ~(y ^ ~x);
        x = (x ^ y);
        System.out.println("x= " + x + ", y=" + y);
    }
}
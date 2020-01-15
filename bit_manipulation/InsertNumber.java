public class InsertNumber {
    public static void main(String[] args) {
        int n = 0b10000011001;
        int m = 0b10011;
        int i = 2;
        int j = 6;
        
        // Create mask.
        int mask = ~0;
        for (int x = i; x <= j; x++) {
            mask ^= (1 << x);
        }
        n &= mask;
        n |= (m << 2);
        System.out.println(Integer.toBinaryString(n));
    }
}
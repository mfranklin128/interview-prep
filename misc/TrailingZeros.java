public class TrailingZeros {
    
    public static int trailingZeros(int n) {
        int nFact = 1;
        int trailing = 0;
        for (int i = 1; i <= n; i++) {
            nFact *= i;
            while (nFact % 10 == 0) {
                nFact = nFact / 10;
                trailing++;
            }
            nFact = nFact % 10;
        }
        return trailing;
    }
    
    public static void main(String[] args) {
        int n = 15;
        System.out.println(trailingZeros(n));
        for (int i = 1; i < n; i++) {
            
        }
    }
}
import java.util.Scanner;

public class Solution {
    static final int MODULUS = 1000000000;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt(); // Number of test cases
        for (int tc = 0; tc < T; tc++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            int e = sc.nextInt();
            int f = sc.nextInt();
            int g = sc.nextInt();
            int h = sc.nextInt();
            long n = sc.nextLong();

            // Compute and print the result
            System.out.println(solve(a, b, c, d, e, f, g, h, n));
        }

        sc.close();
    }

    static String solve(int a, int b, int c, int d, int e, int f, int g, int h, long n) {
        int[] state = initState(); // Initialize the state vector
        int[][] transitionMatrix = buildTransitionMatrix(a, b, c, d, e, f, g, h); // Construct transition matrix
        state = multiplyMod(state, powMod(transitionMatrix, n + 1)); // Compute the new state
        return state[0] + " " + state[11]; // Return the first and twelfth elements of the state vector
    }

    static int[] initState() {
        int[] state = new int[22]; // State vector of size 22

        // Initialize x values (indices 0-8) to 1
        for (int i = 0; i < 9; i++) {
            state[i] = 1;
        }
        state[9] = 0;  // Initialize n * d^n to 0
        state[10] = 1; // Initialize d^n to 1

        // Initialize y values (indices 11-19) to 1
        for (int i = 11; i < 20; i++) {
            state[i] = 1;
        }
        state[20] = 0;  // Initialize n * h^n to 0
        state[21] = 1; // Initialize h^n to 1

        return state;
    }

    static int[][] buildTransitionMatrix(int a, int b, int c, int d, int e, int f, int g, int h) {
        int[][] transitionMatrix = new int[22][22];

        // Transition rules for x values
        transitionMatrix[a - 1][0] = 1;
        transitionMatrix[b + 10][0]++;
        transitionMatrix[c + 10][0]++;
        transitionMatrix[9][0] = 1;

        // Shift values in x
        for (int i = 1; i < 9; i++) {
            transitionMatrix[i - 1][i] = 1;
        }

        transitionMatrix[9][9] = d;
        transitionMatrix[10][9] = d;
        transitionMatrix[10][10] = d;

        // Transition rules for y values
        transitionMatrix[e + 10][11] = 1;
        transitionMatrix[f - 1][11]++;
        transitionMatrix[g - 1][11]++;
        transitionMatrix[20][11] = 1;

        // Shift values in y
        for (int i = 12; i < 20; i++) {
            transitionMatrix[i - 1][i] = 1;
        }

        transitionMatrix[20][20] = h;
        transitionMatrix[21][20] = h;
        transitionMatrix[21][21] = h;

        return transitionMatrix;
    }

    static int[][] powMod(int[][] base, long exponent) {
        int size = base.length;
        int[][] result = buildEntityMatrix(size);
        while (exponent != 0) {
            if ((exponent & 1) != 0) {
                result = multiplyMod(result, base);
            }
            base = multiplyMod(base, base);
            exponent >>= 1;
        }
        return result;
    }

    static int[][] multiplyMod(int[][] matrix1, int[][] matrix2) {
        int size = matrix1.length;
        int[][] result = new int[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                for (int k = 0; k < size; k++) {
                    result[i][j] = addMod(result[i][j], multiplyMod(matrix1[i][k], matrix2[k][j]));
                }
            }
        }
        return result;
    }

    static int[] multiplyMod(int[] vector, int[][] matrix) {
        int size = vector.length;
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                result[i] = addMod(result[i], multiplyMod(vector[j], matrix[j][i]));
            }
        }
        return result;
    }

    static int[][] buildEntityMatrix(int size) {
        int[][] result = new int[size][size];
        for (int i = 0; i < size; i++) {
            result[i][i] = 1;
        }
        return result;
    }

    static int addMod(int x, int y) {
        return (x + y) % MODULUS;
    }

    static int multiplyMod(int x, int y) {
        return (int) ((long) x * y % MODULUS);
    }
}
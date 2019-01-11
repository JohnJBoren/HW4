public class WeirdSort {
    public static int counter1 = 0;

    public static void main(String[] args) // Sort a sample array
    {
        int a[] = { 10, 121, 20, 60, 4, 87, 122 };
        sort(a, a.length);
        // Output the sorted array
        System.out.println();
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");
        System.out.println(
                "\n\nThis program has a worst-case runtime of: \tO(n!).\nI would call this Algorithm:\t\t\tPermutationSort.");
        System.out.println(
                "\nIt experiences the worst-case when the largest number is in the last index of the array.\nConversely the best-case is when the largest number is in the 0th index of the array.");
    }

    // Returns true if the input is sorted.
    private static boolean isSorted(int a[]) {

        System.out.println("Round: " + counter1);
        counter1++;
        for (int i = 0; i < a.length; i++)
            System.out.print(a[i] + " ");

        for (int j = a.length - 1; j > 0; j--) {
            if (a[j] < a[j - 1])
                return false;
        }
        return true;
    }

    // Sorts the array a where n is an index into a starting at the end
    private static boolean sort(int[] a, int n) {
        if (n == 1)
            return (isSorted(a));

        for (int i = 0; i < n; i++) {
            swap(a, i, n - 1);
            if (sort(a, n - 1))
                return true;
            swap(a, i, n - 1);
        }
        return false;
    }

    private static void swap(int[] a, int i, int j) {
        int t;
        t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
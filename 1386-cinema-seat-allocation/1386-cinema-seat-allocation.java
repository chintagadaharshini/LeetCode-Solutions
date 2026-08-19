import java.util.*;

class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {

        // Store reserved seats row-wise
        Map<Integer, Set<Integer>> map = new HashMap<>();

        for (int[] seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];

            map.computeIfAbsent(row, k -> new HashSet<>()).add(col);
        }

        // Every completely empty row can fit 2 groups:
        // [2,3,4,5] and [6,7,8,9]
        int answer = (n - map.size()) * 2;

        // Process only rows having reserved seats
        for (Set<Integer> reserved : map.values()) {

            boolean left = true;   // 2,3,4,5
            boolean middle = true; // 4,5,6,7
            boolean right = true;  // 6,7,8,9

            for (int seat : reserved) {

                if (seat >= 2 && seat <= 5)
                    left = false;

                if (seat >= 4 && seat <= 7)
                    middle = false;

                if (seat >= 6 && seat <= 9)
                    right = false;
            }

            if (left && right) {
                // Can place two groups
                answer += 2;
            } 
            else if (left || middle || right) {
                // Can place one group
                answer += 1;
            }
        }

        return answer;
    }
}
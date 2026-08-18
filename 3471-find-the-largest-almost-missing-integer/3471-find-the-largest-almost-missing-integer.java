import java.util.*;

class Solution {
    public int largestInteger(int[] nums, int k) {

        HashMap<Integer, Integer> count = new HashMap<>();

        // Generate every subarray of size k
        for (int i = 0; i <= nums.length - k; i++) {

            // Store distinct elements of this subarray
            HashSet<Integer> set = new HashSet<>();

            for (int j = i; j < i + k; j++) {
                set.add(nums[j]);
            }

            // Count this subarray for each distinct element
            for (int x : set) {
                count.put(x, count.getOrDefault(x, 0) + 1);
            }
        }

        // Find largest element appearing in exactly one subarray
        int answer = -1;

        for (int x : count.keySet()) {
            if (count.get(x) == 1) {
                answer = Math.max(answer, x);
            }
        }

        return answer;
    }
}
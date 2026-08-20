import java.util.*;

class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;

        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        // First operation
        arr1.add(nums[0]);

        // Second operation
        arr2.add(nums[1]);

        // Remaining elements
        for (int i = 2; i < n; i++) {
            if (arr1.get(arr1.size() - 1) > arr2.get(arr2.size() - 1)) {
                arr1.add(nums[i]);
            } else {
                arr2.add(nums[i]);
            }
        }

        // Combine arr1 + arr2
        int[] result = new int[n];
        int index = 0;

        for (int x : arr1) {
            result[index++] = x;
        }

        for (int x : arr2) {
            result[index++] = x;
        }

        return result;
    }
}
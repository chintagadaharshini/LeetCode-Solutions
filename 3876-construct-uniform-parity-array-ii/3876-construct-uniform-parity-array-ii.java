class Solution {
    public boolean uniformArray(int[] nums1) {

        int min = nums1[0];
        boolean hasOdd = false;

        for (int num : nums1) {
            min = Math.min(min, num);

            if (num % 2 != 0) {
                hasOdd = true;
            }
        }

        // Smallest is odd -> make everything odd
        if (min % 2 != 0) {
            return true;
        }

        // Smallest is even
        // If there is an odd number, impossible
        return !hasOdd;
    }
}
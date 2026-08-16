class Solution {
    public boolean stoneGameIX(int[] stones) {
        int[] count = new int[3];

        // Count stones based on remainder when divided by 3
        for (int stone : stones) {
            count[stone % 3]++;
        }

        // Try Alice taking a remainder-1 stone first
        return check(count[0], count[1], count[2])
            // Try Alice taking a remainder-2 stone first
            || check(count[0], count[2], count[1]);
    }

    private boolean check(int zero, int one, int two) {

        // Alice must start with a 1 (or 2 in the second call)
        if (one == 0) {
            return false;
        }

        one--;

        // Alternating sequence: 1, 2, 1, 2...
        int pairs = Math.min(one, two);

        int length = 1 + pairs * 2;

        one -= pairs;
        two -= pairs;

        // If extra '1' stones exist, one more move can be made
        if (one > 0) {
            length++;
            one--;
        }

        // 0-mod-3 stones don't change the remainder,
        // but they change whose turn it is.
        length += zero;

        // If the sequence has odd length and stones remain,
        // Bob is forced to make the losing move.
        return length % 2 == 1 && (one + two > 0);
    }
}
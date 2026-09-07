class Solution {
    public int distinctSubseqII(String s) {
        long MOD = 1000000007;

        long[] dp = new long[s.length() + 1];
        int[] last = new int[26];

        dp[0] = 1; // empty subsequence

        for (int i = 1; i <= s.length(); i++) {
            int ch = s.charAt(i - 1) - 'a';

            dp[i] = (2 * dp[i - 1]) % MOD;

            if (last[ch] != 0) {
                dp[i] = (dp[i] - dp[last[ch] - 1] + MOD) % MOD;
            }

            last[ch] = i;
        }

        // Remove empty subsequence
        return (int)((dp[s.length()] - 1 + MOD) % MOD);
    }
}
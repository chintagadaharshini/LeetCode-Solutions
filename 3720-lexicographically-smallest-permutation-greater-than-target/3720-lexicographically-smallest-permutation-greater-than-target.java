class Solution {
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();

        // Frequency of characters in s
        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        // Try making the answer greater at position i
        for (int i = n - 1; i >= 0; i--) {

            // We need frequencies after using target[0...i-1]
            int[] remaining = freq.clone();

            boolean possible = true;

            for (int j = 0; j < i; j++) {
                int x = target.charAt(j) - 'a';

                if (remaining[x] == 0) {
                    possible = false;
                    break;
                }

                remaining[x]--;
            }

            if (!possible) {
                continue;
            }

            int current = target.charAt(i) - 'a';

            // Find smallest character greater than target[i]
            for (int c = current + 1; c < 26; c++) {

                if (remaining[c] > 0) {
                    StringBuilder ans = new StringBuilder();

                    // Keep target prefix
                    for (int j = 0; j < i; j++) {
                        ans.append(target.charAt(j));
                    }

                    // Make this position greater
                    ans.append((char) ('a' + c));
                    remaining[c]--;

                    // Put everything else in sorted order
                    for (int j = 0; j < 26; j++) {
                        while (remaining[j] > 0) {
                            ans.append((char) ('a' + j));
                            remaining[j]--;
                        }
                    }

                    return ans.toString();
                }
            }
        }

        return "";
    }
}
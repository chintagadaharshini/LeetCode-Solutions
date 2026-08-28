import java.util.*;

class Solution {
    public String lexPalindromicPermutation(String s, String target) {

        int n = s.length();

        int[] freq = new int[26];

        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        // Check if palindrome is possible
        int odd = 0;
        char middle = 0;

        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                odd++;
                middle = (char) ('a' + i);
            }
        }

        if (odd > 1) {
            return "";
        }

        int halfLen = n / 2;

        int[] halfFreq = new int[26];

        for (int i = 0; i < 26; i++) {
            halfFreq[i] = freq[i] / 2;
        }

        /*
         * STEP 1:
         * Try using exactly target's first half.
         *
         * This is important because the middle or second half
         * can make the palindrome greater than target.
         */
        int[] remaining = halfFreq.clone();
        StringBuilder half = new StringBuilder();

        boolean possible = true;

        for (int i = 0; i < halfLen; i++) {
            int c = target.charAt(i) - 'a';

            if (remaining[c] == 0) {
                possible = false;
                break;
            }

            remaining[c]--;
            half.append((char) ('a' + c));
        }

        if (possible) {
            String palindrome = makePalindrome(
                half.toString(), middle, n
            );

            if (palindrome.compareTo(target) > 0) {
                return palindrome;
            }
        }

        /*
         * STEP 2:
         * Exact first half didn't work.
         *
         * Find the smallest first half that is strictly
         * greater than target's first half.
         */
        for (int pos = halfLen - 1; pos >= 0; pos--) {

            remaining = halfFreq.clone();

            boolean prefixPossible = true;

            // Match target prefix before pos
            for (int i = 0; i < pos; i++) {

                int c = target.charAt(i) - 'a';

                if (remaining[c] == 0) {
                    prefixPossible = false;
                    break;
                }

                remaining[c]--;
            }

            if (!prefixPossible) {
                continue;
            }

            int targetChar = target.charAt(pos) - 'a';

            // Choose the smallest available character
            // greater than target[pos]
            for (int c = targetChar + 1; c < 26; c++) {

                if (remaining[c] > 0) {

                    StringBuilder newHalf = new StringBuilder();

                    // Target prefix
                    for (int i = 0; i < pos; i++) {
                        newHalf.append(target.charAt(i));
                    }

                    // Greater character
                    newHalf.append((char) ('a' + c));
                    remaining[c]--;

                    // Smallest possible remaining characters
                    for (int j = 0; j < 26; j++) {
                        while (remaining[j] > 0) {
                            newHalf.append((char) ('a' + j));
                            remaining[j]--;
                        }
                    }

                    String palindrome = makePalindrome(
                        newHalf.toString(), middle, n
                    );

                    return palindrome;
                }
            }
        }

        return "";
    }

    private String makePalindrome(String half, char middle, int n) {

        StringBuilder result = new StringBuilder();

        result.append(half);

        if (n % 2 == 1) {
            result.append(middle);
        }

        result.append(new StringBuilder(half).reverse());

        return result.toString();
    }
}
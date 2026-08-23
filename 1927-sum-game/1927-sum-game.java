class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int half = n / 2;

        int sum = 0;
        int count = 0;

        for (int i = 0; i < n; i++) {
            char ch = num.charAt(i);

            if (ch == '?') {
                if (i < half)
                    count++;
                else
                    count--;
            } else {
                if (i < half)
                    sum += ch - '0';
                else
                    sum -= ch - '0';
            }
        }

        // Odd number of unmatched '?' -> Alice can always win
        if (count % 2 != 0)
            return true;

        // Bob can win only if the difference can be exactly balanced
        return sum != -count * 9 / 2;
    }
}
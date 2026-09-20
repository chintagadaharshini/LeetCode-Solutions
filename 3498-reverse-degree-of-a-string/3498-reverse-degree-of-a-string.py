class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            # Normal alphabet position: a=1, b=2, ..., z=26
            normal = ord(s[i]) - ord('a') + 1

            # Reverse alphabet position
            reverse = 27 - normal

            # String position is i+1
            ans += reverse * (i + 1)

        return ans
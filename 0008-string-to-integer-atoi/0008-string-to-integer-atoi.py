class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        if not s:
            return 0

        sign = 1
        st_index = 0
        num = 0

        if s[0] == '-':
            sign = -1
            st_index += 1
        elif s[0] == '+':
            st_index += 1

        for i in range(st_index, len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            else:
                break

        num *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN

        return num

        
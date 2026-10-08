class Solution:
    def removeOuterParentheses(self, s):
        ans = []
        depth = 0

        for ch in s:
            if ch == '(':
                # If depth > 0, this is NOT the outermost '('
                if depth > 0:
                    ans.append(ch)
                depth += 1

            else:
                depth -= 1

                # If depth > 0, this is NOT the outermost ')'
                if depth > 0:
                    ans.append(ch)

        return ''.join(ans)
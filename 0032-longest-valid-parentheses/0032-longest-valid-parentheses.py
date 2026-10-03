class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        count=0
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count=max(count ,i-stack[-1])
        return count
        
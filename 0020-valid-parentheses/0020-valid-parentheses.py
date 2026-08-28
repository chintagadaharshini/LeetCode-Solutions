class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match_map={')':'(',']':'[','}':'{'}
        for c in s:
            if c in match_map:
                if not stack or stack.pop()!=match_map[c]:
                    return False
            else:
                    stack.append(c)
        return len(stack)==0

        
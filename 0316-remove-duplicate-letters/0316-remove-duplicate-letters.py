class Solution(object):
    def removeDuplicateLetters(self, s):
        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        stack = []
        visited = set()

        for ch in s:

            # One occurrence is being processed
            freq[ch] -= 1

            # Skip if already in answer
            if ch in visited:
                continue

            # Remove larger characters if they appear later
            while stack and ch < stack[-1] and freq[stack[-1]] > 0:
                visited.remove(stack.pop())

            # Add current character
            stack.append(ch)
            visited.add(ch)

        return "".join(stack)
        
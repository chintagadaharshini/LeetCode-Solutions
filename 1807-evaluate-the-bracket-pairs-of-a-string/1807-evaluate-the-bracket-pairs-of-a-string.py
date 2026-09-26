class Solution(object):
    def evaluate(self, s, knowledge):
        values = {}

        for key, value in knowledge:
            values[key] = value

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                j = s.index(')', i)
                key = s[i + 1:j]

                result.append(values.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1

        return ''.join(result)
        
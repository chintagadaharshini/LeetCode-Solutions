class Solution(object):
    def braceExpansionII(self, expression):
        index = [0]

        def multiply(a, b):
            return {x + y for x in a for y in b}

        def parse():
            result = set()
            current = {""}

            while index[0] < len(expression) and expression[index[0]] != '}':
                ch = expression[index[0]]

                if ch == ',':
                    result |= current
                    current = {""}
                    index[0] += 1

                elif ch == '{':
                    index[0] += 1
                    nested = parse()
                    current = multiply(current, nested)

                else:
                    current = multiply(current, {ch})
                    index[0] += 1

            result |= current

            if index[0] < len(expression) and expression[index[0]] == '}':
                index[0] += 1

            return result

        return sorted(parse())
from collections import defaultdict, deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)
        suspicious = set()
        q = deque([k])

        while q:
            node = q.popleft()

            if node in suspicious:
                continue

            suspicious.add(node)

            for nei in graph[node]:
                if nei not in suspicious:
                    q.append(nei)
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Step 3: Remove suspicious methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans
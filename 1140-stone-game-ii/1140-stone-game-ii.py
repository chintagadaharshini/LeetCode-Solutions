class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            # Can take all remaining piles
            if i >= n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            # Alice wants to maximize her stones
            # Bob will minimize what Alice can get
            for X in range(1, 2 * M + 1):

                # Stones Alice gets from this move
                current = suffix[i] - suffix[i + X]

                # What remains for Bob
                bob = solve(i + X, max(M, X))

                # Alice eventually gets:
                # current + whatever she gets later
                # Total remaining - Bob's best
                total = suffix[i] - solve(i + X, max(M, X))

                best = max(best, total)

            dp[(i, M)] = best
            return best

        return solve(0, 1)
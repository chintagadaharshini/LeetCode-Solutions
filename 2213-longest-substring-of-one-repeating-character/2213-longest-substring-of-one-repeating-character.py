class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)
        tree = [None] * (4 * n)

        def merge(a, b):
            # [left_char, right_char, prefix, suffix, best, length]
            a_left, a_right, a_pref, a_suff, a_best, a_len = a
            b_left, b_right, b_pref, b_suff, b_best, b_len = b

            # Prefix
            prefix = a_pref
            if a_pref == a_len and a_right == b_left:
                prefix = a_len + b_pref

            # Suffix
            suffix = b_suff
            if b_suff == b_len and a_right == b_left:
                suffix = b_len + a_suff

            # Longest repeating substring
            best = max(a_best, b_best)

            # Join suffix of left + prefix of right
            if a_right == b_left:
                best = max(best, a_suff + b_pref)

            return [
                a_left,
                b_right,
                prefix,
                suffix,
                best,
                a_len + b_len
            ]

        def build(node, left, right):
            if left == right:
                ch = s[left]
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, ch):
            if left == right:
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, ch)
            else:
                update(node * 2 + 1, mid + 1, right, index, ch)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):
            update(
                1,
                0,
                n - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            ans.append(tree[1][4])

        return ans
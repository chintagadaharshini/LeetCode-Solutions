class Solution:
    def averageOfSubtree(self, root):
        self.count = 0

        def dfs(node):
            if node is None:
                return 0, 0

            # Get sum and count from left subtree
            left_sum, left_count = dfs(node.left)

            # Get sum and count from right subtree
            right_sum, right_count = dfs(node.right)

            # Include current node
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            # Check average
            if node.val == total_sum // total_count:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count
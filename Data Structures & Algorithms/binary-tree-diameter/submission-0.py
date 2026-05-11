
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def get_height(node):
            if not node:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        get_height(root)
        return self.res
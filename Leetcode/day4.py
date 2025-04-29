class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node: TreeNode) -> (TreeNode, int):
            if not node:
                return (None, 0)
            left_lca, left_depth = helper(node.left)
            right_lca, right_depth = helper(node.right)
            
            if left_depth > right_depth:
                return (left_lca, left_depth + 1)
            elif right_depth > left_depth:
                return (right_lca, right_depth + 1)
            else:

                return (node, left_depth + 1)
        return helper(root)[0]
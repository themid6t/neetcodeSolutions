# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # dfs through the tree and swap left and right nodes
    if not root: return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
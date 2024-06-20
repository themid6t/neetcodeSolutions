from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root) -> int:
    if not root: return 0
    level = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        level += 1
    return level


# def maxDepth(root) -> int:
#     """Depth first search"""
#     if not root: return 0

#     return 1 + max((maxDepth(root.left), maxDepth(root.right)))
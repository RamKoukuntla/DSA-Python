#https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs (node, currentSum):
            if not node:
                return False
            currentSum += node.val
            if not node.left and not node.right:
                return currentSum == targetSum
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        return dfs(root, 0)
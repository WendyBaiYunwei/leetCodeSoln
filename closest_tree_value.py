# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min = (abs(root.val - target), root.val)
        
        def findMin(min, root):
            if root == None:
                return min[1]
            curr = root.val
            if abs(curr-target) < min[0]:
                min = (abs(curr-target), root.val)
            if target < curr:
                return findMin(min, root.left)
            else:
                return findMin(min, root.right)
                
        minVal = findMin(min, root)
        return minVal
'''
Question: 111
Title: Minimum Depth of Binary Tree
Difficulty: Easy

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

'''

def minDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
        return min(left, right) + 1
'''
Question No : 104
Title : Maximum Dpeth of a Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
'''

def MaxDepth(root) -> int:
    if not root:
        return -1
    
    left = MaxDepth(root.left)
    right = MaxDepth(root.right)

    return max(left, right) + 1
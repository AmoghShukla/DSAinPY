'''
Question No. : 226
Title : Invert Binary Tree
Difficulty : Easy

Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]


'''

def invertTree(self, root):
    if not root:
        return None
    
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)

    self.left, self.right = right, left

    return root

root = [4,2,7,1,3,6,9]
print(invertTree(root))
'''
Question No. : 102
Title : Binary Tree Level Order Traversal
Difficulty : Medium

Given the root of a binary tree, return the level order traversal of its nodes' values' (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''
from collections import deque
def levelOrder(self, root):

    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()

            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


root = [3,9,20,None,None,15,7]
print(levelOrder(root))
'''
Question No. : 101
Title : Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

'''

def isSymmetric(root) -> bool:

    if not root:
        return True
    
    def isMirror(t1, t2):

        if not t1 and not t2:
            return True
        
        if not t1 or not t2:
            return False
        
        return (
            t1.val == t2.val and
            isMirror(t1.left, t2.right) and 
            isMirror(t1.right, t2.left)
        )
    
    return isMirror(root.left, root.right)

root = [1,2,2,3,4,4,3]
print(isSymmetric(root))
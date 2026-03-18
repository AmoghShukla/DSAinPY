

def invertTree(self, root):
    if not root:
        return None
    
    left = self.invertTree(root.left)
    right = self.invertTree(root.right)

    self.left, self.right = right, left

    return root
# class TreeNode:
#     def __init__(self, value):
#         self.value=value
#         self.left=None
#         self.right=None
        
#     def inorder(self, root):
#         return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

#     def preorder(self,root):
#         return [root.value] + self.preorder(root.left) + self.preorder(root.right) if root else []

#     def postorder(self,root):
#         return self.postorder(root.left) + self.postorder(root.right) + [root.value] if root else []

# tree = TreeNode (8)
# tree.left = TreeNode (3)
# tree.right = TreeNode(10)
# tree.left.left = TreeNode(1)
# tree.left.right = TreeNode (6)
# print('Inorder Traversal:', tree.inorder(tree))
# print("Preorder Traversal:", tree.preorder(tree))
# print("Postorder traversal:", tree.postorder(tree))


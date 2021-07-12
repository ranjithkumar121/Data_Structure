class node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(str(root.val) + "->",end=" ")
            self.inorder(root.right)


    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.val) + "->", end='')

    def preorder(self,root):
        if root:
            print(str(root.val) + "->", end='')
            self.preorder(root.left)
            self.preorder(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print("Inorder traversal :",end=" ")
root.inorder(root)
print("\nPreorder traversal: ",end=" ")
root.preorder(root)
print("\nPostorder traversal: ",end=" ")
root.postorder(root)

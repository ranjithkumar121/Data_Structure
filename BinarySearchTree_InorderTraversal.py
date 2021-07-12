class Tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def add_child(self,data):
        if data==self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Tree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Tree(data)


    def in_order_traversal(self):
        elements=[]
        #visit left sub tree
        if self.left:
            elements+=self.left.in_order_traversal()
        #visit root node
        elements.append(self.data)
        #visit right sub tree
        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = Tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.in_order_traversal())


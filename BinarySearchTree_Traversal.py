class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left=Tree(data)
        if data>self.data:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right=Tree(data)

    def in_order(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order()
        return elements

    def pre_order(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order()
        if self.right:
            elements+=self.right.pre_order()
        return elements

    def post_order(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order()
        if self.right:
            elements+=self.right.post_order()
        elements.append(self.data)
        return elements



def build_tree(elements):
    root=Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root


if __name__=='__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("In order traversal: ",numbers_tree.in_order())
    print("Pre order traversal: ",numbers_tree.pre_order())
    print("Post order traversal: ",numbers_tree.post_order())


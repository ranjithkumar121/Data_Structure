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

    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.left:
                return self.right.search(val)
            else:
                return False



def build_tree(elements):
    root = Tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.search(21))
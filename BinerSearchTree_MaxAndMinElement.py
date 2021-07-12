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

    def Findmin(self):
        if self.left is None:
            return self.data
        return self.left.Findmin()

    def Findmax(self):
        if self.right is None:
            return self.data
        return self.right.Findmax()

    def calculate_sum(self):
        left_sum=0
        right_sum=0
        if self.left:
            left_sum=self.left.calculate_sum()
        if self.right:
            right_sum=self.right.calculate_sum()
        return self.data+left_sum+right_sum





def build_tree(elements):
    root = Tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    print("Min element: ",numbers_tree.Findmin())
    print("Max element: ",numbers_tree.Findmax())
    print("Sum: ",numbers_tree.calculate_sum())
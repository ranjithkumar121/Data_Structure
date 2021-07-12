class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

    def push(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node

    def ListLenght(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(7)

print("Created Linked List: ")
llist.printList()
c=llist.ListLenght()
print("\nThe lenght of the list is ",c)
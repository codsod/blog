class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def delete(self,value):
        if self.head is None:
            return
        
        if self.head.value==value:
            self.head==self.head.next
        else:
            current=self.head
            while current.next:
                if current.next.value==value:
                    current.next=current.next.next
                    break
                current=current.next
    
    def display(self):
        current=self.head
        while current:
            print(current.value,end=" ")
            current=current.next
        print()
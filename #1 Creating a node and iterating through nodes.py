class Node:
    def __init__(self,data):
        self.data = data
        self.next = ""

class LinckedList:
    def __init__(self):
        self.head = ""
    def interator(self):
        if self.head == "":
            print("Lincked List is Empty")
        nn = self.head
        while nn !="":
            print(nn.data)
            nn = nn.next

ll = LinckedList()
ll.interator()
            

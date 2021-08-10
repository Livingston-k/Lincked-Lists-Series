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
        lst = ""
        while nn !="":
            lst += str(nn.data)+"-->"
            nn = nn.next
        print(lst)
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

ll = LinckedList()
ll.add_begin(12)
ll.add_begin(11)
ll.add_begin(10)
ll.add_begin(6)
ll.interator()
            
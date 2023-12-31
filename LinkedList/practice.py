class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
                print(temp.value)
                temp = temp.next
    #append
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1


ll = LinkedList(5)
ll.print_list()
ll.append(10)
ll.print_list()
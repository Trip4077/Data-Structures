
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def view_queue(self):
        self.storage.print()
       

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0: return

        node = self.storage.head

        self.storage.remove_from_head()
        self.size -= 1

        return node.value

    def len(self):
        return self.size

# my_queue = Queue()

# my_queue.enqueue(1)
# my_queue.enqueue(9)
# my_queue.enqueue(7)

# my_queue.dequeue()

# my_queue.view_queue()
# print( "Size: " + str( my_queue.len() ) )

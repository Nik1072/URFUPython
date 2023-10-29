class EmptyQueueException(Exception):
    pass

class Queue:
    class Node:  # Вспомогательный класс для узлов списка
        def __init__(self, data=None, next_node=None, previous_node=None):
            self.data = data
            self.next = next_node
            self.prev = previous_node

    def __init__(self):
        self.head = Queue.Node()
        self.tail = Queue.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length_of_queue = 0

    def enqueue(self, value):
        new_node = Queue.Node(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length_of_queue += 1

    def dequeue(self):
        if self.length_of_queue == 0:
            raise EmptyQueueException
        remove_node = self.tail.prev
        self.tail.prev = remove_node.prev
        remove_node.prev.next = remove_node.next
        return_value = remove_node.data
        remove_node.next = None
        remove_node.prev = None
        self.length_of_queue -= 1
        return return_value
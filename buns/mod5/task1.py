# Исключение для пустого стека
class EmptyStackException(Exception):
    pass

class Stack:
    class Node: # Вспомогательный класс для узлов списка
        def __init__(self, data, next_element):
            self.element_data = data
            self.next_element = next_element

    def __init__(self):
        self.top_element = None

    def push(self, data):
        self.top_element = Stack.Node(data, self.top_element)

    def pop(self):
        if not (self.top_element is None):
            current_element = self.top_element.element_data
            self.top_element = self.top_element.next_element
            return current_element
        else:
            raise EmptyStackException

    def peek(self):
        if not (self.top_element is None):
            return self.top_element.element_data
        else:
            raise EmptyStackException
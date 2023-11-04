# Исключение для случая, если индекс переданный методу
# отсутствует в списке
class IndexIsNotInLinkedList(Exception):
    pass


class Node:
    def __init__(self, data, next_element, index):
        self.node_data = data
        self.next_node = next_element
        self.index_node = index


class LinkedList:
    def __init__(self):
        self.element = None
        self.index_of_element = 0
        self.iter_element = self.element
        self.update_iter_element = False

    def __next__(self):
        if self.iter_element is None:
            if self.update_iter_element:
                self.update_iter_element = False
                raise StopIteration
            else:
                self.iter_element = self.element
                self.update_iter_element = True
        current_iter_element = self.iter_element
        self.iter_element = self.iter_element.next_node
        return current_iter_element.node_data

    def __iter__(self):
        return self

    def push(self, val):
        self.element = Node(val, self.element, self.index_of_element)
        self.index_of_element += 1

    def get(self, index):
        if (self.index_of_element - 1) < index:
            raise IndexIsNotInLinkedList

        current_element = self.element

        while current_element.index_node != index:
            current_element = current_element.next_node
        return current_element.node_data

    def remove(self, index):
        if (self.index_of_element - 1) < index:
            raise IndexIsNotInLinkedList

        current_element = self.element
        self.index_of_element -= 1

        if self.element.index_node == index:
            self.element = self.element.next_node
        elif (current_element.index_node - 1) == index:
            current_element.index_node -= 1
            next_element = current_element.next_node
            current_element.next_node = next_element.next_node
        else:
            while (current_element.index_node - 1) != index:
                current_element.index_node -= 1
                current_element = current_element.next_node
            next_element = current_element.next_node
            current_element.index_node -= 1
            current_element.next_node = next_element.next_node

    # Как я понял, номер элемента (n) принят за индекс элемента.
    # Я допустил возможность вставлять элемент в самое начало
    # списка (т.е. когда n = 0), хоть и n-1 элемента технически
    # не существует. В тоже время я запретил вставлять элемент
    # за верхние пределы списка, даже просто в конец списка
    # (т.е. когда n > максимального индекса в списке)
    def insert(self, n, val):
        if (self.index_of_element - 1) < n:
            raise IndexIsNotInLinkedList

        current_element = self.element
        self.index_of_element += 1

        if self.element.index_node == n:
            new_element = Node(val, self.element.next_node, n)
            self.element.next_node = new_element
            self.element.index_node += 1
        else:
            while current_element.index_node != n:
                current_element.index_node += 1
                current_element = current_element.next_node
            new_element = Node(val, current_element.next_node, n)
            current_element.next_node = new_element
            current_element.index_node += 1
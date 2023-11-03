class DoubleElement:
    def __init__(self, *lst):
        self.list = lst
        self.current_index = 0

    def __next__(self):
        if self.current_index == len(self.list):
            raise StopIteration
        first = self.list[self.current_index]
        self.current_index += 1
        if self.current_index == len(self.list):
            return first, None
        second = self.list[self.current_index]
        self.current_index += 1
        return first, second

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)

dL = DoubleElement()
for pair in dL:
    print(pair)

# Ожидаемый результат кода:
# (1, 2)
# (3, 4)
#
# (1, 2)
# (3, 4)
# (5, None)
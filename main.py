

list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

# -------------------Задание №1-------------------------------

class FlatIterator:
    cursor = 0
    cursor_index = -1

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list  

    def __iter__(self):
        
        return self

    def __next__(self):
        self.cursor_index += 1
        while self.cursor_index > len(self.list_of_list[self.cursor]) - 1:
            self.cursor += 1
            self.cursor_index = 0
            if self.cursor > len(self.list_of_list) - 1:
                raise StopIteration
        return self.list_of_list[self.cursor][self.cursor_index]



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


for item in FlatIterator(list_of_lists_1):
    print(item)


# ------------------Конец-------------------------------------------

print()

# -------------------Задание №2-------------------------------

import types


def flat_generator(list_of_lists):

    for item_1 in list_of_lists:
        for item_2 in item_1:
            yield item_2



def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

for item in flat_generator(list_of_lists_1):
    print(item)



# -------------------------Конец----------------------------------
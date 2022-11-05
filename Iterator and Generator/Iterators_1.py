# Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает
# их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в коде ниже также
# должна отработать без ошибок.

list_of_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:

    def __init__(self, list_of_list):
        self.start = -1
        self.end = len(list_of_list)


    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return ' '.join(str(elem) for elem in list_of_list[self.start])


for item in FlatIterator(list_of_list):
    print(item)

def test():

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
    test()
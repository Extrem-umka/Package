# Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.
# Шаблон и тест в коде ниже:

list_of_list = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_of_list_cursor = 0
        self.list_of_list_cursor_1 = 0 # список вложенный в основной список list_of_list
        return self

    def __next__(self):
        self.list_of_list_cursor_1 += 1
        if self.list_of_list_cursor_1 > len(self.list_of_list_cursor_1):
            self.list_of_list_cursor += 1
            self.list_of_list_cursor = 0
        if self.list_of_list_cursor > len(self.list_of_list_cursor):
            raise StopIteration
        return self.list_of_list[self.list_of_list_cursor][self.list_of_list_cursor_1]

for item in FlatIterator(list_of_list):
    print(item)

def test():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test()
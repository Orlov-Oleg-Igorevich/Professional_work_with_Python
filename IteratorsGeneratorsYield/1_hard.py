class Error:
    pass

class EndList:
    pass


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.count_list = []

    def __iter__(self):
        n = self.list_of_list
        while isinstance(n, list):
            n = n[0]
            self.count_list.append(0)
        return self

    def get_nesting(self):
        item = self.list_of_list
        try:
            for i in self.count_list:
                item = item[i]
        except IndexError:
            del self.count_list[-1]
            self.count_list.append(self.count_list.pop(-1)+1)
            if len(self.count_list) == 1 and self.count_list[0] >= len(self.list_of_list):
                return EndList
            return Error

        while isinstance(item, list):
            if len(item) == 0:
                self.count_list.append(self.count_list.pop(-1)+1)
                return Error
            item = item[0]
            self.count_list.append(0)
        self.count_list.append(self.count_list.pop(-1)+1)

        return item



    def __next__(self):
        response = self.get_nesting()
        while response in {EndList, Error}:
            if response == EndList:
                raise StopIteration
            response = self.get_nesting()
        return response


def test_3():

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

        assert list(FlatIterator(list_of_lists_2)) == [
            'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
            ]


if __name__ == '__main__':
    test_3()

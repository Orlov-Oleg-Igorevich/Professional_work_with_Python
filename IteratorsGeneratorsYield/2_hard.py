import types

class Error:
    pass

class EndList:
    pass

def get_nesting(list_of_list, count_list):
    item = list_of_list
    try:
        for i in count_list:
            item = item[i]
    except IndexError:
        del count_list[-1]
        count_list.append(count_list.pop(-1)+1)
        if len(count_list) == 1 and count_list[0] >= len(list_of_list):
            return EndList
        return Error

    while isinstance(item, list):
        if len(item) == 0:
            count_list.append(count_list.pop(-1)+1)
            return Error
        item = item[0]
        count_list.append(0)
    count_list.append(count_list.pop(-1)+1)

    return item

def generator(list_of_list, count_list):
    response = get_nesting(list_of_list, count_list)
    while response in {EndList, Error}:
        if response == EndList:
            return EndList
        response = get_nesting(list_of_list, count_list)
    return response

def flat_generator(list_of_list):
    n = list_of_list
    count_list = []
    while isinstance(n, list):
        n = n[0]
        count_list.append(0)
    while (ans := generator(list_of_list, count_list)) != EndList:
        yield ans



def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
        ]

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()

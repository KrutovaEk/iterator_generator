import types


def flat_generator(list_of_lists):
    list_of_lists = list_of_lists
    i = 0
    next = list_of_lists[i]
    while True:
        i +=1
        for item in next:
            yield item
        if i >= len(list_of_lists):
            break
        next = list_of_lists[i]
    
# list_of_lists_1 = [
#       ['a', 'b', 'c'],
#        ['d', 'e', 'f', 'h', False],
#        [1, 2, None]
# ]

# f= list(flat_generator(list_of_lists_1))
# print(f)


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
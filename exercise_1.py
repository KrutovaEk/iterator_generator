class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.i=0
        self.next = self.list_of_list[self.i]
        self.list = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.list)
        except StopIteration:
            if self.i>=len(self.list_of_list):
                raise StopIteration
            self.next = self.list_of_list[self.i]
            self.list = iter(self.next)
            item = next(self.list)
            self.i +=1
        return item
            
        
# list_of_lists_1 = [
#        ['a', 'b', 'c'],
#        ['d', 'e', 'f', 'h', False],
#        [1, 2, None]
#    ]

# for i in FlatIterator(list_of_list=list_of_lists_1):
#     print(i)

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
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: linked_list.py.py
@time: 2021/3/23
@desc:
'''


class Node (object):
    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_


class flatten_linked_list():
    def __init__(self):
        assert isinstance(self._value, int) or isinstance(self._value, Node)
        assert isinstance(self._next, Node) or (self.next_ == None)
        if self.next_ == None:
            pass

    @property
    def value(self):
        return self._value

    @property
    def next_(self):
        return self._next

    # def __repr__(self):
    #     return str(self.value)

    # def __iter__(self):
    #     print("the value is:", self.value,
    #           "             the next value is:", self._next)
    #     while self._next is not None:
    #         print(self._next == None)
    #         return iter(self._next)

    # def flatten_linked_list(self, node):
    #     while node is not None:
    #         yield node
    #         node = node.next

    # print(node.value,node.next_)


if __name__ == '__main__':

    # r1 = Node ( 1 ) # 1 -> None - just one node
    r2 = Node(7, Node(2, Node(9)))  # 7 -> 2 -> 9 -> None
    # for i in r2:
    #     print(i)
    # # # 3 -> (19 -> 25 -> None ) -> 12 -> None
    # r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
    # r3_flattenned = Node.flatten_linked_list(r3)  # 3 -> 19 -> 25 -> 12 -> None
    # r3_expected_flattenned_collection = [3, 19, 25, 12]
    # # print(list( r3_flattenned ))
    # assert r3_expected_flattenned_collection == list(r3_flattenned)

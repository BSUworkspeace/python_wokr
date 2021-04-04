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


class flatten_linked_list(object):
    def __init__(self, node):
        assert isinstance(node._value, int) or isinstance(node._value, Node)
        assert isinstance(node._next, Node) or (node._next == None)
        self.node = node

    @property
    def _value(self):
        print(self.node._value)
        return self.node._value

    @property
    def _next(self):
        print(self.node._next)
        return self.node._next

    def __iter__(self):
        current = self._next
        while current is not None:
            yield scurrent
            current = scurrent._next

    # def flatten_linked_list(self, node):
    #     while node is not None:
    #         yield node
    #         node = node.next

    # print(node.value,node.next_)


if __name__ == '__main__':

    # r1 = Node ( 1 ) # 1 -> None - just one node
    r2 = Node(7, Node(2, Node(9)))  # 7 -> 2 -> 9 -> None
    print(r2._next)
    for i in flatten_linked_list(r2):
        print(i)
        # # # 3 -> (19 -> 25 -> None ) -> 12 -> None
        # r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
        # r3_flattenned = Node.flatten_linked_list(r3)  # 3 -> 19 -> 25 -> 12 -> None
        # r3_expected_flattenned_collection = [3, 19, 25, 12]
        # # print(list( r3_flattenned ))
        # assert r3_expected_flattenned_collection == list(r3_flattenned)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: linked_list.py.py
@time: 2021/3/23
@desc:
'''

class Node ( object ):
    def __init__ ( self , value , next_ = None ):
        self._value = value
        self._next = next_

        assert isinstance(self._value, int ) or isinstance(self._value, Node )
        assert isinstance(self._next, Node ) or (self.next_ == None)

    @property
    def value(self):
        return self._value
    @property
    def next_( self):
        return self._next

    def __iter__(self):
        print("the value is:",self.value,"             the next value is:",self._next)
        try:
            return iter(self._next)
        except:
            return None



def flatten_linked_list(node):
    while 1:
        try:
            x = iter(node)
            x.value
        except TypeError:
            break
    # print(node.value,node.next_)
if __name__ == '__main__':

    # r1 = Node ( 1 ) # 1 -> None - just one node
    # r2 = Node (7 , Node (2 , Node ( 9 ) ) ) # 7 -> 2 -> 9 -> None
    # # # 3 -> (19 -> 25 -> None ) -> 12 -> None
    r3 = Node(3,Node(Node(19,Node(25)),Node(12)))
    r3_flattenned = flatten_linked_list(r3) # 3 -> 19 -> 25 -> 12 -> None
    r3_expected_flattenned_collection = [3 , 19 , 25 , 12]
    # print(list( r3_flattenned ))
    assert r3_expected_flattenned_collection == list( r3_flattenned )
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: iter_helpers.py.py
@time: 2021/3/21
@desc:
'''
def transpose(iterables:list)->list:
    import itertools

    return list(itertools.zip_longest(*iterables))

def scalar_product(scalar1:list , scalar2:list)->any:


    try:
        return    sum(list(map(lambda e, f: int(e) * int(f), scalar1, scalar2)))

    except ValueError:
        return None


expected = 1
actual = scalar_product([1, '2'], [-1, 1])
assert expected == actual
actual = scalar_product([1, 'xyz'], [-1, 1])
assert actual is None

expected = [[1 , 2], [-1 , 3]]
actual = transpose ([[1 , -1], [2 , 3]])
assert expected == list (map(list , actual ) )
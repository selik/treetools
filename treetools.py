#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Utilities for tree data structures, such as data parsed from JSON
documents.

'''

from collections.abc import Mapping


def traverse(tree):
    '''

    Iterator of every key-value pair in a collection of nested
    dictionaries, depth-first.

        >>> t = {'a': 1, 'b': {'c': 2}, 'd':  3}
        >>> list(traverse(t))
        [('a', 1), ('b', {'c': 2}), ('c', 2), ('d', 3)]
    
    '''
    for key, value in tree.items():
        yield key, value
        if isinstance(value, Mapping):
            yield from traverse(value)


def search(tree, key):
    '''

    Search for a value by key in a collection of nested dictionaries,
    depth-first.  Returns the value of the first matching key, ignorning
    duplicates.

        >>> t = {'a': 1, 'b': {'c': 2}, 'c':  3}
        >>> search(t, 'c')
        2

    Raises KeyError if the target key is not found in the tree.

    '''
    for k, value in traverse(tree):
        if key == k:
            return value
    raise KeyError(key)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

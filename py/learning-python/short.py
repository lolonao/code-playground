"""Tips & Tricks"""
elements = ['A', 'B', 'C', 'D']
numbers = [1, 2]

zipped = zip(numbers, elements)
print(list(zipped))  # [(1, 'A'), (2, 'B')]

from itertools import zip_longest
zipped = zip_longest(numbers, elements)
print(list(zipped))  # [(1, 'A'), (2, 'B')]

zipped = zip_longest(numbers, elements, fillvalue='_')
print(list(zipped))  # [(1, 'A'), (2, 'B'), ('_', 'C'), ('_', 'D')]


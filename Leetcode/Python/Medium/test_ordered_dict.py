from collections import OrderedDict

ordered_dict = OrderedDict(
    [('a', 'A'), ('b', 'B'), ('c', 'C')]
)
print(ordered_dict)
ordered_dict.move_to_end('b', last=False)
print(ordered_dict)
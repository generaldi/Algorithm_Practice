import sys
an_int = 4242424
print(sys.getsizeof(an_int))
an_int = 4242424424242442424244242424
print(sys.getsizeof(an_int))
a_float = 3.1442424242
print(sys.getsizeof(a_float))
list_example = [[1,2,3],[1,2,3]]
for row in list_example:
    for element in row:
        print(id(element))
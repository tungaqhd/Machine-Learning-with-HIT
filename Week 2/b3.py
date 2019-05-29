my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
key = [i for i in my_dict.keys()]
def cmp(a):
    return my_dict[a]
key.sort(key=cmp)
print(key)
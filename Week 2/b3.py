my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}
key = [i for i in my_dict.keys()]
key.sort(key=my_dict.get)
print(key)
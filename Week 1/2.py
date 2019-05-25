import json
def get_name(path):
    arr = path.strip().split('/')
    return arr[-1]
file = open('data/path.txt')
wr = open('data/path.json', 'w')
add = list()
ch = dict()
for path in file:
    ch['path'] = path.strip().replace('\n', '')
    ch['file_name'] = get_name(path)
    add.append(ch.copy())
json.dump(add, wr)

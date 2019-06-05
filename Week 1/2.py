import json
def get_name(path):
    arr = path.strip().split('/')
    return arr[-1]
file = open('data/path.txt')
wr = open('data/path.json', 'w')
add = list()
ch = dict()
for path in file:
    add.append({'path': path.strip().replace('\n', ''), 'file_name': get_name(path)})
json.dump(add, wr, indent=4)

file.close()
wr.close()

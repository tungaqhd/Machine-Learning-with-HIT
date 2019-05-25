import json
import os
def get_name(path):
    arr = path.strip().split('/')
    return arr[-1]
class Path:
    def input_path(self):
        self.path = input('Input path: ').strip()

    def output(self):
        print('Invalid Path')

    def valid_path(self, path):
        if os.path.exists(path):
            return True
        else:
            return False
    def write_json(self, data):
        json_file = open('data/path.json', 'w')
        json.dump(data, json_file)

tung = Path()
tung.input_path()
if not tung.valid_path( tung.path ):
    tung.output()
else:
    ch = dict()
    add = list()
    file = open(tung.path)
    for path in file:
        ch['valid'] = tung.valid_path(path)
        ch['path'] = path
        ch['file_name'] = get_name(path)
        add.append(ch.copy())
    tung.write_json(add)
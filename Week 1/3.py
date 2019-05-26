import json
import os
def get_name(path):
    arr = path.strip().split('/')
    return arr[-1]
class Path:
    def __init__(self):
        self.__path = ''
        self.__file_name = ''
    def input_path(self):
        self.__path = input('Input path: ').strip()
        self.__file_name = get_name(self.__path)

    def output(self):
        f = open('data/path.txt')
        print('Full Path:')
        for path in f:
            print(path.strip())

    def valid_path(self, path):
        if path == '':
            path = self.__path
        if os.path.exists(path):
            return True
        else:
            return False

    def append_json(self):
        # read from .txt
        add = list()
        file = open(self.__path)
        for path in file:
            add.append({'valid': tung.valid_path(path), 'path': path, 'file_name': get_name(path)})
        file.close()
        # collect old data
        with open('data/path.json') as file:
            old_data = json.load(file)
        # append data
        old_data.extend(add)
        file.close()
        print('New Json data: \n', old_data)
        file = open('data/path.json', 'w')
        json.dump(old_data, file)

tung = Path()
tung.input_path() # tested with data/path.txt
if not tung.valid_path(''):
    print('Invalid Path')
else:
    tung.output()
    tung.append_json()
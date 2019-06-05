def get_name(path):
    arr = path.strip().split('/')
    return arr[-1]
if __name__ is '__main__':
    path = input()
    print(get_name(path))
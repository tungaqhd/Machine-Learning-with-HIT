path = input()
def get_name(path):
    arr = path.split('/')
    return arr[-1]
print(get_name(path))
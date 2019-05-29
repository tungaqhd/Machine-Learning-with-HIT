s = input()
W = int(input())
tmp = ''
for i in range(0, len(s), W):
    tmp += s[ i : i + min(len(s)-i, W) ] + '\n'
s = tmp
print(s)
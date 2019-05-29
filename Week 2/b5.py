def pal(s):
    try:
        check = s.islower()
        return s == s[::-1]
    except:
        return TypeError('S must be a string')
s = input()
print(pal(s))
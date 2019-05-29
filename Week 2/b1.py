for i in range(1, 101):
    if i%3 is 0 and i%5 is 0:
        print('fizzbuzz')
    elif i%3 is 0:
        print('fizz')
    elif i%5 is 0:
        print('buzz')
    else:
        print(i)
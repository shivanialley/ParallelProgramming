'''
map()
'''

def fun(arg):
    return f'{arg} passed to fun()'


if __name__ == '__main__':
    res = map(fun,[1,2,3,4,5,6])
    for i in res:
        print(i)


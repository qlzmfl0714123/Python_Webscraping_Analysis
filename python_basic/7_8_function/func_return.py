def swap(x,y):
    return y,x

r = swap(100,200)
print(r)
print(type(r))


def myfunc(name):
    msg = 'Hello ' + name
    return msg
    print('리턴한 후에 출력됨')
    
result = myfunc('홍길동')
print(result)
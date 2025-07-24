def times(a=10,b=20):
    return a * b

x = times()
y = times(5)
z = times(b=30)
print(x,y,z)

#tuple parameter
def tuple_param(*p):
    return p

result = tuple_param(1,2,4,5,)
print(type(result),result)

#dict parameter
def dict_param(**p):
    for key,value in p.items():
        print(key,':',value)

dict_param(id=100,name='길동',age=30)

#다중값 return
def swap(a,b):
    return b,a

a = swap(1,2)
x, y = swap(3,4)

print(type(a),a)
print(x,y)

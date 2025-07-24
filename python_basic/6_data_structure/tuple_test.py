mytuple = (1,2,3,4)
print(type(mytuple))
print(mytuple[1])
print(mytuple*2)
mytuple = (10,10,20)
print(mytuple)
#TypeError: 'tuple' object does not support item assignment
#mytuple[1] = 30

t1 = (1)
t2 = (1,)
print(type(t1),type(t2))
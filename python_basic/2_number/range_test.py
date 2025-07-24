r1 = range(1,10,2)
print(type(r1))
print(r1)
print(list(r1))

for v in r1:
    print(v)

print(list(range(2,-1,1)))

for x in range(2,-1,-1):
    print(x)

mylist = list(range(200,250,10))
print(mylist)

num = 100
num2 = 103.34

print('정수형 ',num)
print('정수형 값은 %d' %num)
print('실수형 값은 %0.2f' %num2)
print('=>실수형 값은 %d' %num2)
print('정수형 값은 %s' %num)

print(f'정수형 값은{num} 실수형 값은 {num2:.2f}')
print(f'금액은 = {price:,}')

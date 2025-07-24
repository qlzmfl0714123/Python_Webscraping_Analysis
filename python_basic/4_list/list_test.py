#packing
my_list = [1,2,3,4]
#unpacking
n1,n2,n3,n4 = my_list
print(f'n1={n1} n2={n2} n3={n3} n4={n4}')

my_list2 = [5,6,7,8,6]
my_list2[0] = 40    # item 1개를 인덱스 0에 교체 
my_list2.append(10) # item 1개를 맨 끝에 추가
print(my_list2)
my_list2.extend(my_list) # list에 다른 list 추가
print(my_list2)

# for item1 in my_list:
#     for item2 in my_list2:
#         print(item1,item2)

print(my_list.pop(1))
print(my_list)

del my_list2[1]
print(my_list2)
del my_list2[1:3] #인덱스 1,2인 아이템이 삭제됨
print(my_list2)

value1 = 10
value2 = 10,
print(f'value = {type(value1)} value2={type(value2)}')

#tuple 생성(Packing)
movie = 'superman',1987,'batman',1989,
print(type(movie))

#tuple 항목별 할당(unpacking)
t1,y1,t2,y2 = movie
print(t1,y1,t2,y2)
print(type(y1))

my_tuple = (10,20,30)
print(type(my_tuple))
#TypeError: 'tuple' object does not support item assignment
#my_tuple[0] = 40

#tuple 활용
def swap(n1,n2):
    return (n2,n1)

a,b = swap(20,30)
print(a,b)

# set 은 중복을 허용하지 않는다.
my_set = {'java','python','java','c++',}
print(my_set)
#my_set2 = my_set['java'] = 'Java'
#print(my_set2)

my_list = [4,3,5,1,3]
#my_set = set(my_list)
#print(my_set)
my_list = list(set(my_list))
print(my_list)

set1 = {'a','b','c'}
set2 = {'b','d','e'}
#차집합
result = set1 - set2
print(result)
#여집합
result = set1 ^ set2
print(result)

#dict 선언
my_dict = {}
print(type(my_dict))
my_dict = dict()
print(type(my_dict))

#dict 선언 및 초기화 
my_dict = {'red':10,'blue':5,'red':20,'Red':40,'Orange':100}
print(my_dict)
keys = my_dict.keys()
print(type(keys))
print(sorted(keys))

values = my_dict.values()
print(type(values))
items = my_dict.items()
print(type(items))

# keys() 함수를 사용해서 dict key와 value 출력하기
for key in my_dict.keys():
    print(f"키 = {key} 값 = {my_dict[key]}")

#items()함수를 사용해서 dict key와 value 출력하기
for key,value in my_dict.items():
    print(f"키 = {key} Calue = {value}")
    
#값 변경
my_dict['red'] = 30
print(my_dict)
# key 존재 여부 확인
print('blue' in my_dict)
print(my_dict)

#값이 존재하는지 여부 체크
print(40 in my_dict.values())

#키가 존재하는지 여부 체크
print('red' in my_dict)
print('red' in my_dict.keys())
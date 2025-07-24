mydict = {300:'둘리',200:'고길동',100:'마이콜'}
print(mydict)
print(mydict[300])
mydict[400] = '등장인물1'
print(mydict)
print(mydict.get(200))

del mydict[100]
print(mydict)
print(200 in mydict)

mydict2 = {}
mydict2['lang3'] = 'scalar'
mydict2['lang1'] = 'java'
mydict2['lang2'] = 'python'
print(mydict2)
mydict2['lang3'] = '자바스크립트'
print(mydict2)
print(mydict2.get('lang2'))
print(mydict2.get('lang4'))

#해당 키가 없을 경우에 에러 발생함
#print(mydict2['lang4'])

value = mydict2.get('lang4')
#None 은 데이터가 없다는 뜻이고, 조건식에서 False와 같음
if value:
    print(value)
else:
    print('키가 존재하지 않음')

print('lang3' in mydict2)

mylist = ['c1','c2','r3']
print(dict(mylist))
# mylist = ['a200','b500','c600']
# print(dict(mylist))


print(mydict.keys())
print(mydict.values())
print(mydict.items())

for key in mydict.keys():
    #print(key,' = ',mydict[key])
    print(key,' = ',mydict.get(key))

for k,v in mydict2.items():
    print(k,' = ',v)
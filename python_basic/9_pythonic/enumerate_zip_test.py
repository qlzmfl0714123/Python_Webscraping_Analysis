for idx,val in enumerate(['abc','yyy','www']):
    print(idx,val)

langs = ['java','python','c#']
print(list(enumerate(langs)))

str1 = 'I like pythonic coding style'.split()
mylist = [[idx,val] for idx,val in enumerate(str1)]
print(mylist)
mydict = {idx:val.upper() for idx,val in enumerate(str1)}
print(mydict)

a1,a2,a3= zip((1,2,3),(10,20,30),(100,200,300))
print(a1,a2,a3)

result = [x for x in zip((1,2,3),(10,20,30),(100,200,300))]
print('=>',result)

result = [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
print(result)

result = {idx:sum(x) for idx,x in enumerate(zip((1,2,3),(10,20,30),(100,200,300))) }
print(result)

a,b,c = zip(['a','b','c'],['A','B','C'])
print(a,b,c)

list1 = [w for w in zip(['a','b','c'],['A','B','C'])]
print('=>',list1)

list2 = [[i,w] for i,w in enumerate(zip(['a','b','c'],['A','B','C']))]
print('=>2',list2)

dict1 = {i:w for i,w in enumerate(zip(['a','b','c'],['A','B','C']))}
print('=>3',dict1)

dict2 = {i:(w1+w2) for i,(w1,w2) in enumerate(zip(['a','b','c'],['A','B','C']))}
print('=>4',dict2)

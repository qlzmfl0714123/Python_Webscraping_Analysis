#split
langs = 'python,java,c#,scalar'
a,b,c,d = langs.split(',')

print(a,b,c,d)

items = 'zero one two three four'.split()
print(items)

#join
colors = ['red','yellow','blue']
result = '/'.join(colors)
print(result)

#list comprehension
values = [i for i in range(10)]
print(values)

values = [i for i in range(10) if i % 2 == 0]
print(values)

values = [i if i % 2 == 0 else 10 for i in range(20)]
print(values)

word1 = 'Hello'
word2 = 'World'
result = [i+j for i in word1 for j in word2]
print(result)

case1 = ['A','B','C']
case2 = ['D','E','A']
result = [i+j for i in case1 for j in case2 if i != j]
print(result)

#enumerate
for idx, val in enumerate(['tic','tac','toc']):
    print(idx,val)

result = list(enumerate(['tic','tac','toc']))
print(result)

result = {i:j for i,j in enumerate('My lime orange tree'.split())}
print(result)

print("zip test")
#zip
list1 = ['a','b','d']
list2 = ['a1','b1','d1','e1']

for a,b in zip(list1,list2):
    print(a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)

result = [sum(i) for i in zip((1,2,3),(10,20,30),(100,200,300))]
print(result)
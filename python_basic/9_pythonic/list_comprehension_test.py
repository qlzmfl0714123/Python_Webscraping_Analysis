result=[]
for i in range(10):
    result.append(i)
print(result)

result2 = [j for j in range(10)]
print(result2)

result3 = [k for k in range(50) if k % 3 == 0]
print(result3)

word1="Hello"
word2="World"
result = [i+j for i in word1 for j in word2 if not(i==j)]
print(result)

str1 = 'I like pythonic coding style'.split()
print('===========')
print(str1)

result = [[w.upper(),w.lower(),len(w)] for w in str1]
print(result)

for r in result:
    print(r)


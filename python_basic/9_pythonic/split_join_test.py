items = 'zero one two three'.split()
print(items)

langs = 'python,java,c#'
a,b,c = langs.split(',')
print(a,b,c)

url='mail.google.com'
d1,d2,d3 = url.split('.')
print(d1,d2,d3)

colors = ['red','yellow','blue']
result= ''.join(colors)
print(result)
result= ' '.join(colors)
print(result)
result= ', '.join(colors)
print(result)

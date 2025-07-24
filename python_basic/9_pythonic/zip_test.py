days=['월','화','수']
coffees=['아메리카노','라떼','모카']
fruits=['바나나','딸기','사과','귤']

#print(zip(days,coffees,fruits))

for a,b,c in zip(days,coffees,fruits):
    print(a,b,c)

for i,(d,f) in enumerate(zip(days,fruits)):
    print(i,d,f)


print(list(zip(days,coffees,fruits)))
print(dict(zip(days,coffees)))

a = [('a','b'),('c','r')]
print(a)


user1={'id':1,'name':'홍길동','email':'hong@aa.com','phone':'010-1234-5678'}
user2={'id':2,'name':'이순신','email':'lee@aa.com','phone':'010-1231-5671'}
user3={'id':3,'name':'장영실','email':'jang@aa.com','phone':'010-1232-5672'}
user4={'id':4,'name':'김홍도','email':'kim@aa.com','phone':'010-5231-9671'}
user5={'id':5,'name':'세종','email':'jj@aa.com','phone':'010-5231-9671',
       'hobby':['독서','등산','영화']}

users=[user1,user2,user3,user4,user5]

# print(users)
# print(users[3])

for user in users:
    #print(user)
    for key,value in user.items():
        print(key,'=',value)
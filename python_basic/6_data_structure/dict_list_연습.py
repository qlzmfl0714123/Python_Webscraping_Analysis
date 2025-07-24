users = [{'id':1,'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-1234'},
         {'id': 2, 'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-2343-1234'}]
#users[0] = {'id':1,'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-1234'}

users.append({'id': 3, 'name': 'hong kildong3', 'email': 'hong@mail.com3', 'hp_num': '010-2343-1233'})

print(users)

for user in users:
    for key in user.keys():
        print(key ,"=", user[key])

print('items() 사용 ---------------------------------')
for user in users:
    for key,value in user.items() :
        print(key, "=", value)
        
        

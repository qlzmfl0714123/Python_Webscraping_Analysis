#태어난 연도를 입력 받아서 나이를 계산하여
#어떤 학생인지를 출력한다.

from datetime import datetime as dt

print(dt.today())
print(dt.today().year)
print(dt.today().day)

current_year = dt.today().year
print('현재년도 :',current_year)
input_year = int(input('태어난 년도를 입력하세요'))
age = current_year - input_year + 1
print('나이는 ',age)

if 17 <= age < 20:
    print('고등학생입니다.')
elif 20 <= age < 30:
    print('대학생입니다.')
elif (age >= 8) and (age <= 13):
    print('초등학생입니다')
else:
    print('학생이 아닙니다.')
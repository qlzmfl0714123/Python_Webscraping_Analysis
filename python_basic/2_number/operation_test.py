def operation(num1,num2,op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return num1/num2
    else:
        print('Ivalid operator')
        return 0

def main():
    num1= int(input('숫자1을 입력하세요'))
    num2= int(input('숫자2을 입력하세요'))
    print(operation(num1,num2,'+'))
    print(operation(num1,num2,'*'))
    print(operation(num1,num2,'-'))
    print(operation(num1,num2,'/'))

main()

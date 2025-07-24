# for i in range(10):
#     result = 10/i
#     print(i,result)


for i in range(10):
    try:
        result = 10/i
    except Exception as err:
        print("error 발생됨", err)
    except ArithmeticError as arr:
        print("연산 에러 발생", arr)
    else:
        print(i,result)
    finally:
        print(i,'반드시 출력되어야하는 코드')


#chapter13장에 too_big_num_error_class 에 raise 구문 사용한 예제 있음
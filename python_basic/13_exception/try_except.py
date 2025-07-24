def my_func():
    try:
        print('Hello python'+ 2)
    except Exception as exp:
        #에러 메시지 출력
        print(exp.args)
        print('예외발생 {}'.format(exp))
        import traceback
        traceback.print_exc()
    finally:
        print('exception 발생후 출력됨')

my_func()
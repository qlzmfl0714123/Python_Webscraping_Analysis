"""
섭씨 온도를 입력 받아서 화씨 온도로 변환하는 모듈
"""
def convert(c):
    #float() 함수는 str -> float 타입으로 변환
    fah = ((9/5) * float(c)) + 32
    return fah


def sayHello(name):
    return "Hello "+name

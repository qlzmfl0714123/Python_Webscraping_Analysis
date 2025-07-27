def greet(name="이름없음", greeting="안녕하세요", postfix="님!"):
    return f"{greeting}, {name}{postfix}"

# 예시 출력
print(greet("김철수"))
print(greet("John", greeting="Hello", postfix="!"))
print(greet("이영희", postfix="님! 좋은 하루 되세요!"))
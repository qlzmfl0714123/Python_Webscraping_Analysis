#평균값을 구하는 함수 선언
def average(numbers):
    total = 0
    for num in numbers:
        total += num
    avg = total / len(numbers)
    return avg

def main():
    prices = [100,200,100]
    result = average(prices)
    print(result)
    print(type(result))
    print('평균값은 %d'%result)

main()
def average(numbers):
    total = 0;
    for num in numbers:
        total += num

    avg = total / len(numbers)
    return round(avg)

# prices = [2450,3600,4500,2100]
# result = average(prices)
# print('평균 : ' , result)

def main():
    prices = [2450, 3600, 4500, 2100]
    result = average(prices)
    print('평균 : ', result)

main()
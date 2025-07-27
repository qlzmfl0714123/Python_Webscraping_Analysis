import math

def get_statistics(numbers):
    avg = sum(numbers) / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = round(math.sqrt(variance), 2)
    return avg, maximum, minimum, std_dev

# 예시 출력
data = [10, 20, 30, 40, 50]
avg, max_val, min_val, std = get_statistics(data)

print("숫자들:", data)
print("평균:", avg)
print("최댓값:", max_val)
print("최솟값:", min_val)
print("표준편차:", std)
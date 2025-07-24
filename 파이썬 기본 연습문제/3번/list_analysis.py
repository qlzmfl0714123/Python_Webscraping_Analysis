numbers = [15, 3, 27, 8, 19, 12, 31]
print("숫자 목록:", numbers)

max_val = max(numbers)
min_val = min(numbers)
second_max = sorted(numbers, reverse=True)[1]

print("최댓값:", max_val)
print("최솟값:", min_val)
print("두 번째로 큰 값:", second_max)
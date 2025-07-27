numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원본 숫자:", numbers)

squared = list(map(lambda x: x**2, numbers))
print("모든 수의 제곱:", squared)

filtered = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 수들:", filtered)

filtered_squared = list(map(lambda x: x**2, filtered))
print("5보다 큰 수들의 제곱:", filtered_squared)
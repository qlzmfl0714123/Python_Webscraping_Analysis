numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원본 숫자:", numbers)

<<<<<<< HEAD
squared = list(map(lambda x: x ** 2, numbers))
print("모든 수의 제곱:", squared)

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 수들:", greater_than_5)

squared_filtered = list(map(lambda x: x ** 2, greater_than_5))
print("5보다 큰 수들의 제곱:", squared_filtered)
=======
squared = list(map(lambda x: x**2, numbers))
print("모든 수의 제곱:", squared)

filtered = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 수들:", filtered)

filtered_squared = list(map(lambda x: x**2, filtered))
print("5보다 큰 수들의 제곱:", filtered_squared)
>>>>>>> f50fafb87ee121d035b4304f29b910e371c1f160

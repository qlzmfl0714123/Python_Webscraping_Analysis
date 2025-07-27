score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

<<<<<<< HEAD
nums = [5, -2, 12, -8, 0, 23, -1, 42]
max_num = max(nums)
print(f"숫자들의 최대값: {max_num}")

positive_nums = [n for n in nums if n > 0]
print(f"양수들: {positive_nums}")
=======
numbers = [13, 7, 42, 23]
max_value = numbers[0] if not numbers else max(numbers)
print(f"숫자들의 최대값: {max_value}")

positives = [n for n in numbers if n > 0]
print("양수들:", positives)
>>>>>>> f50fafb87ee121d035b4304f29b910e371c1f160

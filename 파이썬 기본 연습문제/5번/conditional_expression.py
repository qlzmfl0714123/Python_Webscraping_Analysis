score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

nums = [5, -2, 12, -8, 0, 23, -1, 42]
max_num = max(nums)
print(f"숫자들의 최대값: {max_num}")

positive_nums = [n for n in nums if n > 0]
print(f"양수들: {positive_nums}")
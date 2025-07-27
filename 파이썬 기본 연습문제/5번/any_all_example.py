number1 = [2, 4, 6, 8, 10]
number2 = [1, 3, 5, 7, 12]

print("숫자 리스트:", number1)
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in number1))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in number1))

print("\n숫자 리스트2:", number2)
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in number2))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in number2))
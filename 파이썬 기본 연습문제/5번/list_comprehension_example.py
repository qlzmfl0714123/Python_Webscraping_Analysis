numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원본 리스트:", numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print("짝수들:", even_numbers)

squared_evens = [n**2 for n in even_numbers]
print("짝수의 제곱:", squared_evens)
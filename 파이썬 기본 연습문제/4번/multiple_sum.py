multiples = [i for i in range(1, 101) if i % 3 == 0]
total = sum(multiples)

print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {total}")
print(f"3의 배수의 개수: {len(multiples)}개")
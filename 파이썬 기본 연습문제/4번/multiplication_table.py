how = int(input("몇 단을 출력할까요? "))
print(f"{how}단 구구단:")

for i in range(1, 10):
    print(f"{how} x {i} = {how * i}")
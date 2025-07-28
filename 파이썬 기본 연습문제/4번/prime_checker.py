num = int(input("숫자를 입력하세요: "))

if num < 2:
<<<<<<< HEAD
    print(f"{num}은 소수가 아닙니다.")
=======
    is_prime = False
>>>>>>> f50fafb87ee121d035b4304f29b910e371c1f160
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

<<<<<<< HEAD
    if is_prime:
        print(f"{num}은 소수입니다.")
    else:
        print(f"{num}은 소수가 아닙니다.")
        
=======
if is_prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")
>>>>>>> f50fafb87ee121d035b4304f29b910e371c1f160

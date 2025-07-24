print("변환하고 싶은 섭씨 온도를 입력해 주세요:")
user_input = input()
print(type(user_input))

fah = ((9/5) * float(user_input)) + 32

print("섭씨 온도 : ",user_input)
print("화씨 온도 : ",round(fah,2))
print("홧씨 온도 : {}".format(fah))
print("화씨 온도 : {0:.2f}".format(fah))
print(f"화씨 온도 : {fah:.2f}")

email = input("이메일 주소를 입력하세요: ")

username, domain = email.split("@")

print("사용자명:", username)
print("도메인:", domain)
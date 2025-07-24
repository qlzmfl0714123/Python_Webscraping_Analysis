sentence = input("문장을 입력하세요: ")

cleaned = ' '.join(sentence.split())

print("공백 제거:", cleaned)
print("단어 개수:", len(cleaned.split()), "개")
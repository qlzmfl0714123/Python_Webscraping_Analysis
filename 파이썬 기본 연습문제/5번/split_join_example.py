text = "Python is awesome programming language"
print("원본 문자열:", text)

words = text.split()
print("분리된 단어들:", words)

joined_with_hyphen = "-".join(words)
print("하이픈으로 연결:", joined_with_hyphen)

upper_joined = " ".join(word.upper() for word in words)
print("대문자로 변환 후 공백으로 연결:", upper_joined)
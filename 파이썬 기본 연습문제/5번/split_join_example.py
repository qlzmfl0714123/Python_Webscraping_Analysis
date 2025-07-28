text = "Python is awesome programming language"
print("원본 문자열:", text)

words = text.split()
print("분리된 단어들:", words)

<<<<<<< HEAD
hyphen_joined = "-".join(words)
print("하이픈으로 연결:", hyphen_joined)
=======
joined_with_hyphen = "-".join(words)
print("하이픈으로 연결:", joined_with_hyphen)
>>>>>>> f50fafb87ee121d035b4304f29b910e371c1f160

upper_joined = " ".join(word.upper() for word in words)
print("대문자로 변환 후 공백으로 연결:", upper_joined)
from collections import Counter

text = """
파이썬 프로그래밍 언어 언어 언어 배우기 쉬운 쉬운 강력한 파이썬
프로그래밍 언어 배우기 쉬운 언어 강력한 강력한 프로그래밍 쉬운 배우기
배우기 배우기 파이썬
"""

# 단어 분리 및 정제
words = [word.strip(".,!?\n") for word in text.split()]
counter = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in counter.most_common():
    print(f"{word}: {count}번")
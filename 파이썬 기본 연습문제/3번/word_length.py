words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
print("단어 목록:", words)

longest = max(words, key=len)
shortest = min(words, key=len)

print(f"가장 긴 단어: {longest} ({len(longest)}글자)")
print(f"가장 짧은 단어: {shortest} ({len(shortest)}글자)")
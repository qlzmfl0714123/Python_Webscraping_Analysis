import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

filename = "data.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

print("데이터가 data.json에 저장되었습니다.\n")

with open(filename, "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("JSON에서 읽어온 데이터:")
for key, value in loaded_data.items():
    print(f"{key}: {value}")
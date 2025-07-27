import csv

filename = "grades.csv"
grades = [("김철수", 85), ("이영희", 92), ("박민수", 78), ("최수진", 95)]

# CSV 파일에 저장
with open(filename, "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "점수"])
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

# CSV 파일에서 읽고 평균 계산
print("성적 분석 결과:")
total = 0
count = 0
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["이름"]
        score = int(row["점수"])
        print(f"{name}: {score}점")
        total += score
        count += 1

avg = total / count
print(f"전체 평균: {avg:.1f}점")
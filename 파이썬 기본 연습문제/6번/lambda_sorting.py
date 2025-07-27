students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print("학생 정보:", students)

# 이름순 정렬
by_name = sorted(students, key=lambda x: x[0])
print("이름순 정렬:", by_name)

# 점수 오름차순
by_score = sorted(students, key=lambda x: x[1])
print("점수순 정렬:", by_score)

# 점수 내림차순
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print("점수 내림차순:", by_score_desc)
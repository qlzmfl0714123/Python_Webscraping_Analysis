students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

print("학생과 점수 매칭:")
for student, score in zip(students, scores):
    print(f"{student}: {score}점")

score_dict = {student: score for student, score in zip(students, scores)}
print("점수별 학생 딕셔너리:", score_dict)
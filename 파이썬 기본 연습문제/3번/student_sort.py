students = [
    {'이름': '김철수', '나이': 20, '학과': '컴퓨터공학과'},
    {'이름': '박민수', '나이': 21, '학과': '경영학과'},
    {'이름': '이영희', '나이': 22, '학과': '영어영문학과'},
    {'이름': '최수진', '나이': 23, '학과': '수학과'}
]

sorted_students = sorted(students, key=lambda x: x['나이'])

print("나이 순으로 정렬된 학생 목록:")
for student in sorted_students:
    print(f"{student['이름']} ({student['나이']}세) - {student['학과']}")
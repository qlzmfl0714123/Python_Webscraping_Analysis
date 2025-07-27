import datetime

filename = "app.log"
logs = [
    ("2025-07-20 09:15:00", "WARNING", "메모리 사용량이 높습니다"),
    ("2025-07-20 10:30:00", "ERROR", "데이터베이스 연결 실패"),
    ("2025-07-20 11:45:00", "ERROR", "파일을 찾을 수 없음"),
    ("2025-07-20 12:00:00", "WARNING", "디스크 공간 부족"),
    ("2025-07-20 13:00:00", "INFO", "프로세스가 정상적으로 완료되었습니다")
]

with open(filename, "w", encoding="utf-8") as file:
    for time, level, message in logs:
        file.write(f"{time} - {level} - {message}\n")

print("로그 파일이 생성되었습니다.\n")

def filter_logs(level):
    print(f"{level} 레벨 로그들:")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if f" - {level} - " in line:
                print(line.strip())
    print()

filter_logs("ERROR")
filter_logs("WARNING")
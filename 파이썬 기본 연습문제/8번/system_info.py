import os
import sys

print("현재 작업 디렉토리:", os.getcwd())

print("Python 버전:", sys.version)

print("운영체제:", os.name)

path_env = os.environ.get("PATH", "").split(os.pathsep)
print("환경 변수 PATH 일부:", ":".join(path_env[:4]))


path = "/Users/username/documents/report.txt"
directory, filename = os.path.split(path)
filename_noext, ext = os.path.splitext(filename)

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename_noext + ext}")
print(f"- 확장자: {ext}")

print("파일 존재 여부:", os.path.exists(path))
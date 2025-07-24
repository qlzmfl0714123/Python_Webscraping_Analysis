import os
if not os.path.isdir("log"):
    os.mkdir("log")

FILE_NAME = "log/count_log.txt"
print("file writing start")
# if not os.path.exists(FILE_NAME):
#     f = open(FILE_NAME,'w',encoding="utf-8")
#     f.write("파일 기록이 시작됩니다.\n")
#     f.close()

with open(FILE_NAME,'a',encoding="utf-8")as logfile:
    import random
    from datetime import datetime
    for i in range(1,11):
        # stamp = str(datetime.datetime.now())
        stamp = str(datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + " 값이 생성되었습니다. \n"
        logfile.write(log_line)
print("file writing end")

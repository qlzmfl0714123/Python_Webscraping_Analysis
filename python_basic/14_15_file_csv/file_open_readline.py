with open("i_have_a_dream.txt", "r") as my_file:
    i=0
    while True:
        line = my_file.readline()
        if line.strip() != "":
            print(str(i) + "===" + line.strip())
        if not line:
            break
        i = i + 1
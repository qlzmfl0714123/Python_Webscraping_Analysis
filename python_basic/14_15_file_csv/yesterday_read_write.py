import os

#log 폴더가 존재여부 체크해서 없으면 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')

def file_read(file_name):
    my_list = []
    with open(file_name,'r',encoding='utf8') as file:
        content = file.read()
        #print(content)
        my_list = content.split('\n')
    return my_list

def file_read_write(file_name):
    with open(file_name,'r',encoding='utf8') as file:
        content = file.read()
        word_list = content.split(' ')
        line_list = content.split('\n')

        print('글자 갯수 :',len(content))
        print('단어 갯수 :', len(word_list))
        print('라인 갯수 :', len(line_list))

    w_file = open('log/file_info.txt','a',encoding='utf8')
    w_file.write('글자 갯수-'+str(len(content))+'\n')
    w_file.write('단어 갯수-'+str(len(word_list)) + '\n')
    w_file.write('라인 갯수-'+str(len(line_list)) + '\n')
    w_file.close()

FILE_NAME = 'yesterday.txt'
result = file_read(FILE_NAME)
print(result)
result = [i for i in result if len(i) != 0]
print(result)

file_read_write(FILE_NAME)
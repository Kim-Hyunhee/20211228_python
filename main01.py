my_file = open('내파일.txt', 'a')  # a(append) : append 모드

# 주석 추가 - 변경사항 발생
my_file.write('두 줄 내용을 추가합니다.\n')
my_file.write('두 줄 내용을 추가합니다.\n')

my_file.close()
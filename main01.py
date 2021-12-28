my_file = open('내파일.txt', 'w')  # w(write) : write 모드로 파일 열기

my_file.write('안녕하세요.\n')
my_file.write('내가 파이썬으로 만든\n첫 번째 파일입니다.\n')

my_file.close()
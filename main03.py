# 절대 경로 체험

my_file = open('c:\\202112_KHH_Python\\file_test\\test03.txt','r')   # r(read) : 파일 읽어오기 모드

# 파일의 전체 내용이 통째로 필요한 경우
full_data = my_file.read()

print(full_data)

my_file.close()
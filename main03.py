# 절대 경로 체험

my_file = open('c:\\202112_KHH_Python\\file_test\\test03.txt','r')   # r(read) : 파일 읽어오기 모드

line = my_file.readline()

print(line)

line2 = my_file.readline()
print(line2)

my_file.close()
# 파일은 열고 나면 반드시 닫아야함
# 파이썬의 with 문법 이용 => 열고 난 파일을 with 구문이 끝나면 자동 종료

with open('student_list.txt', 'a') as my_file:  # 'a' : 추가 작성이어도 해당 파일이 없다면 생성도 같이 해줌
    my_file.write('이 파일은 학생 목록을 저장합니다.')
    
# with 구문이 끝남
# 여기가 실행된다 : my_file은 자동으로 close 되어있는 상태
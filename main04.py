# 파일은 열고 나면 반드시 닫아야함
# 파이썬의 with 문법 이용 => 열고 난 파일을 with 구문이 끝나면 자동 종료

with open('student_list.txt', 'a') as my_file:  # 'a' : 추가 작성이어도 해당 파일이 없다면 생성도 같이 해줌
    
    # 새 학생을 한 명씩 추가하자
    # 이름, 출생 년도, 거주지 (ex. 서울시 동대문구)
    print('새 학생 추가')
    
    name = input('이름 : ')
    birth_year = int(input('출생 년도 : '))
    address = input('거주지 : ')
    
    # 파일에 한 줄의 문구로 추가 => 이름, 출생 년도, 거주지  한 줄로 가공
    input_line = f'{name}, {birth_year}, {address}\n'   # 한 명을 추가하고, 다음 줄로 내려주자
    print(input_line)
    
    # my_file 변수를 이용해 만들어진 한 줄을 추가해보자
    my_file.write(input_line)  # 줄 바꿈 자동 지원 X
    
    
# with 구문이 끝남
# 여기가 실행된다 : my_file은 자동으로 close 되어있는 상태
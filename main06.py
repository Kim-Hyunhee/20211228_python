from datas.student import Student


with open('student_list.txt', 'r') as f:
    line = f.readline().strip()
    
    # 문제 - 조경진(34세) - 서울시 동대문구 다시 가공해서 출력 => 학생 객체를 만들고 / 기능 활용\
    infos = line.split(',')
    
    student = Student(infos[0], infos[1] ,infos[2])
    
    student.print_studenf_info()   
    
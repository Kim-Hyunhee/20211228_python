# 학생 정보를 담고, 기능들을 가진 클래스

class Student:
    # 학생을 만들 때, 이름 / 출생년도(int) / 거주지를 받아서 세팅해주자
    def __init__(self, name, birth_year, address):
        self.name = name
        self.birth_year = int(birth_year)  # str이 들어온 경우 대비
        self.address = address
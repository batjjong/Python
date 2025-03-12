# class_test_4.py

#한 학생의 성적 처리를 위한 자료형 (Student)
#속성(변수)
#   이름(name), 성적(scores, dict)
#기능(메소드)
#   평균계산(avg), 최고점계산(max), 최저점계산(min)
#   전체정보출력(__str__)

class Student:
    #클래스 변수
    #클래스 당 하나만 생성
    #접근법 : Student.subname
    #수업시간에 설명하지 않음.
    subname = {
        'kor':"국어",
        'eng':"영어",
        'mat':"수학"
    }

    def __init__(self, name, **scores):
        self.name = name
        self.scores = scores

    def avg(self):
        return sum(self.scores.values()) / len(self.scores)

    def max(self):
        return max(self.scores.values())

    def min(self):
        return min(self.scores.values())

    def __str__(self):
        msg = f"이름:{self.name}\n" \
              f"평균:{self.avg():0.2f} \n" \
              f"최고:{self.max()} 최저:{self.min()}\n" \
              f"[전과목성적]\n"

        for sub, score in self.scores.items():
            sub = Student.subname.get(sub, sub)
            msg += f"{sub}:{score}"
            if score == self.max():
                msg += "(+)\n"
            elif score == self.min():
                msg += "(-)\n"
            else:
                msg += "\n"
        return msg

if __name__ == "__main__":
    students = [
        Student("김미영", kor=100, mat=100, eng=100), #왜 모두 (+)가 나오는가?
        Student("이미영", kor=10, mat=10, eng=100, sci=65)
    ]

    for s in students:
        print(s)







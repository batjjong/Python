person = {}
print(type(person))
while True:
    print("===============")
    print("[1] 추가")
    print("[2] 검색")
    print("[0] 종료")
    print("===============")
    a = int(input("선택 : "))

    if a == 1:
        print("추가 기능 수행")
        while True:
            key = input("이름 : ")
            if key.lower() == '':
                print("===연락처목록===")
                for key, value in person.items():
                    print(f"{key} : {value}")
                break
            value = input("연락처 : ")
            person[key] = value

    elif a == 2:
        print("검색 기능 수행")
        key = input("이름:")

        if None != person.get(key):
            print(f"{key}의 연락처:{person[key]}")
        else:
            print("해당 이름의 연락처를 찾을수 없습니다")

    elif a == 0:
        break

    else:
        print("다시 입력해주세요")

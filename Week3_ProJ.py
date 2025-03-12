#1-1번
soc_num = input("주민등록번호:")
a = soc_num[0:6]
b = soc_num[7]
print("연월일:", a)
print("성별:", b)

#1-2번
soc_num = input("주민등록번호:")
a = soc_num[0:6]
b = soc_num[7]
print(f"연월일:{a}")
print(f"성별:{b}")

#2-1번
one = int(input("1st:"))
two = int(input("2nd:"))
thr = int(input("3rd:"))
avr = (one + two + thr)/3
prt = "%.2f" % (avr)
print(prt)

#2-2번
a = int(input("1st:"))
b = int(input("2st:"))
c = int(input("3st:"))
avr = (a + b + c) / 3
print(f"{a},{b},{c}의 평균은 {avr:0.2f}입니다.")

#3번
inmoney = int(input("투입한 돈:"))
thimoney = int(input("물건의 가격:"))

leave = inmoney - thimoney
print("거스름돈:", leave)

won500 = int(leave // int(500))
print("500 동전 개수:", won500)

won100 = int((leave % int(500)) // int(100))
print("100 동전 개수:", won100)

#4-1번
a = input("기호:")
str = input("삽임 분자열:")
prt = a[0] + str + a[1]
print("출력:", prt)

#4-2번
a = input("기호:")
str = input("삽임 분자열:")
print(f"출력:{a[0] + str + a[1]}")


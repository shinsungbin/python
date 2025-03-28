select, answer, cal, num1, num2 = 0, 0, "", 0, 0

select = int(input("1. 입략힌 수식 계산 / 2. 두 수 사이의 합계 :"))

if select == 1:
    cal = input ("수식 입력> ")
    answer = eval(cal)
    print("%s 결과는 %5.1f입니다." % (cal, answer))

elif select == 2:
    num1 = int(input ("숫자1 입력> "))
    num2 = int(input("숫자2 입력> "))
    for i in range(num1, num2 + 1):
        answer = answer + i
    print("%d+...+%d는 %d입니다." % (num1, num2, answer))

else:
    print("1 또는 2만 입력해주세요.")


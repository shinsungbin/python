select = int(input("입력 진수 결정 (10/10/8/2) :"))
num = input("값 입력 : ")

if select == 16:
    num10 = int(num, 16)
if select == 10:
    num10 = int(num, 10)
if select == 8:
    num10 = int(num, 8)
if select == 2:
    num10 = int(num, 2)

print("16진수 ==>", hex(num10))
print("10진수 ==>", num10)
print("8진수 ==>", oct(num10))
print("2진수 ==>", bin(num10))

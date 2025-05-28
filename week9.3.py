from tkinter import *
from time import *

fnameList = ["cat1.gif", "cat2.gif", "cat3.gif", "cat4.gif", "cat5.gif", "cat6.gif", "cat7.gif", "cat8.gif", "cat9.gif"]
photoList = [None] * 9
num = 0

def clickNext(): 
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<< 이전", command = clickPrev)
btnNext = Button(window, text = "다음 >>", command = clickNext)
nameLabel = Label(window, text=fnameList[0], relief="solid")

photo = PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\" + fnameList[0])
pLabel = Label(window, image = photo)

btnPrev.place(x = 250, y = 10)
nameLabel.place(x = 335, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()
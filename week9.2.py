from tkinter import *
import random

btnList = [None] * 9
fnameList = ["cat1.gif", "cat2.gif", "cat3.gif", "cat4.gif", "cat5.gif", "cat6.gif", "cat7.gif", "cat8.gif", "cat9.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

random.shuffle(fnameList)

window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i]=PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\" + fnameList[i])
    btnList[i]=Button(window, image=photoList[i])

for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
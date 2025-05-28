from tkinter import *
window = Tk()

photo1 = PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\cat1.gif")
label1 = Label(window, image=photo1)

label1.pack(side=LEFT)

photo2 = PhotoImage(file="C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\week9\\cat2.gif")
label2 = Label(window, image=photo2)

label2.pack(side=LEFT)

window.mainloop()
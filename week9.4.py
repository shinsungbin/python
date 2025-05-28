from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    key_name = ""
    
    if event.keycode == 37:
            key_name = "Shift + 왼쪽 화살표"
    elif event.keycode == 38:
            key_name = "Shift + 위쪽 화살표"
    elif event.keycode == 39:
            key_name = "Shift + 오른쪽 화살표"
    elif event.keycode == 40:
            key_name = "Shift + 아래쪽 화살표"

    if key_name:
        messagebox.showinfo("키보드 이벤트", "눌린 키: " + key_name)

window = Tk()
window.title("키보드 이벤트")

window.bind("<Key>", keyEvent)

window.mainloop()

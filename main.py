
from tkinter import *
import string
import random

def clicked():
    btn.destroy()
    lbl.destroy()
    ei = str(txt.get())
    letter1 = random.choice(string.ascii_uppercase) 
    letter2 = random.choice(string.ascii_uppercase)
    letter3 = random.choice(string.ascii_uppercase)
    letter4 = random.choice(string.ascii_uppercase)
    first_module = ei[3] + ei[4] + ei[5] + letter1 + letter2
    second_module = ei[0] + ei[1] + ei[2] + letter3 + letter4
    third_module = str(int(ei[3] + ei[4] + ei[5]) + int(ei[0] + ei[1] + ei[2]))
    if len(third_module) < 4:
        third_module = '0' + third_module
    key = first_module + '-' + second_module + ' ' + third_module
    lbl_1 = Label(window, text=key, font=("Times New Roman", 18))
    lbl_1.grid(column=1, row=0)
    txt.destroy()


window = Tk()
window.title('Subway Surf KEY')

window.geometry("1200x675")
bg = PhotoImage(file = "backsubway.png")
label1 = Label(window, image=bg)
label1.place(x = 0, y = 0)
 
# window.geometry("1200x675")
# bg = PhotoImage(file = "Tf16.gif")
# label1 = Label(window, image=bg)
# label1.place(x = 0, y = 0)

lbl = Label(window, text="Please enter a DEC-number of 6 characters: ", font=("Times New Roman", 18))
lbl.grid(column=0, row=0)

txt = Entry(window,width = 10)
txt.grid(column=2, row=0)

btn = Button(window, text="enter", font=("Times New Roman", 18),command=clicked)
btn.grid(column=3, row=0)

window.mainloop()
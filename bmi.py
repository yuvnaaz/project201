from tkinter import *

window = Tk()
window.title('bmi calculator')
window.geometry("400x400")
window.configure(bg = 'yellow')

name_label = Label(window,text = "your name", fg = 'blue', bg = 'yellow', font = ("Calibri", 15))
name_label.place(x = 20, y = 50)

username = Entry(window,text = "", width = 20, borderwidth = 2)
username.place(x = 100,y=50)

height_label = Label(window,text = "your height", fg = 'blue', bg = 'yellow', font = ("Calibri", 15))
height_label.place(x = 20, y = 100)

height = Entry(window,text = "", width = 20, borderwidth = 2)
height.place(x = 100,y=100)

weight_label = Label(window,text = "your weight", fg = 'blue', bg = 'yellow', font = ("Calibri", 15))
weight_label.place(x = 20, y = 150)

weight = Entry(window,text = "", width = 20, borderwidth = 2)
weight.place(x = 100,y=150)

def bmi():
    W = int(weight.get())
    H = int(height.get())/100
    B = W/(H*H)
    B = round(B,2)
    msg = ""
    if B <18.5:
        msg = "Under Weight"
    if B >=18.5 and B<=24.9:
        msg = "Normal"
    if B >=25 and B<=29.9:
        mesg = "obese"
    output = Label(window, text = str(B)+msg, bg = "yellow", font = ("Calibri", 15))
    output.place(x = 100, y= 250)


calculate_button = Button(window, text = "calculate", fg = "black", bg = "yellow", bd = 4, command = bmi)
calculate_button.place(x= 100, y= 200)


window.mainloop()
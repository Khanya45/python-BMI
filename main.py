import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")
root.title("BMI CALCULATOR")
root.config(bg="#EBB3DC")

def BMICalculator():
    if float(edtAge.get()) < 18:
        messagebox.showerror("ERROR", "SORRY YOU DO NOT QUALIFY")
    else :
        BMI = float(edtWeight.get())/(float(edtHeight.get())/100) ** 2
        if BMI < 18:
            edtBMI.insert(0, "UNDERWEIGHT")
        elif BMI >= 18 and BMI < 25:
            edtBMI.insert(0, "NORMAL")

        elif BMI >= 25 and BMI < 30:
            edtBMI.insert(0, "OVERWEIGHT")

        elif BMI >= 30:
            edtBMI.insert(0, "OBESE")

        if lbGender.get() == "MALE":
             IdealBMI= round(0.5 * float(edtWeight.get())/ (float(edtHeight.get()) / 100) ** 2 + 11.5, 2)
             edtIBMI.insert(0, IdealBMI)
        else:
            IdealBMI = round(0.5 * float(edtWeight.get()) / (float(edtHeight.get()) / 100) ** 2 + 0.03 * float(edtAge.get()) + 11, 2)
            edtIBMI.insert(0, IdealBMI)


def clear():
    edtBMI.delete(0, END)
    edtAge.delete(0, END)
    edtWeight.delete(0, END)
    edtIBMI.delete(0, END)
    edtHeight.delete(0, END)
    lbGender.current(0)


def exit():
    root.destroy()


def checkAge():
    if edtAge.get() <18:
        messagebox.showerror("ERROR", "SORRY YOU DO NOT QUALIFY")

canvas = Canvas(root, width = 170, height = 170)
canvas.place(x=220, y=40)
img = ImageTk.PhotoImage(Image.open("BMI.jpg"))
canvas.create_image(0, -50, image=img)

lblweight = Label(root, text="WEIGHT", font="times 12", bg="#EBB3DC")
lblweight.place(x=20, y=50)
edtWeight = Entry(root, width=10)
edtWeight.place(x=120, y=50)

lblheight = Label(root, text="HEIGHT", font="times 12", bg="#EBB3DC")
lblheight.place(x=20, y=90)
edtHeight = Entry(root, width=10)
edtHeight.place(x=120, y=90)


lblage = Label(root, text="AGE", font="times 12", bg="#EBB3DC")
lblage.place(x=20, y=130)
edtAge = Entry(root, width=10)
edtAge.place(x=120, y=130)

lblgender = Label(root, text="GENDER", font="times 12", bg="#EBB3DC")
lblgender.place(x=20, y=170)
lbGender = tkinter.ttk.Combobox(root, height=3, width=10)
lbGender['values'] = ('FEMALE', 'MALE')
lbGender.place(x=120, y=170)

btnCal = Button(root, text="Calculate", command=BMICalculator, width=40)
btnCal.place(y=260, x=30)

lblBMI = Label(root, text="BMI: ", font="times 12", bg="#EBB3DC")
lblBMI.place(x=15, y=300)
edtBMI = Entry(root, width=15)
edtBMI.place(x=50, y=300)

lblIBMI = Label(root, text="Ideal BMI: ", font="times 12", bg="#EBB3DC")
lblIBMI.place(x=190, y=300)
edtIBMI = Entry(root, width=15)
edtIBMI.place(x=270, y=300)

btnClear = Button(root, text="CLEAR", command=clear)
btnClear.place(x=100, y=350)

btnExit = Button(root, text="EXIT", command=exit)
btnExit.place(x=180, y=350)


root.mainloop()

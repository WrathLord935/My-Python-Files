from tkinter import *
import tkinter.font as font

wn = Tk(className=' Cube & Square')
wn.geometry('400x500')
photo = PhotoImage(file = "Square & Cube Icon.png")
wn.iconphoto(True, photo)

font=font.Font(family='Times New Roman', size=16)

def square():
    inp11 = StringVar()
    inp11 = text1.get('1.0', 'end-1c')
    inp11 = int(inp11)
    inp12 = inp11**2
    label2.config(text= inp12)
    print(inp11,'^2 = ',inp12)

def cube():
    inp21 = StringVar()
    inp21 = text2.get('1.0', 'end-1c')
    inp21 = int(inp21)
    inp22 = inp21**3
    label4.config(text= inp22)
    print(inp21,'^3 = ',inp22)

def sqrt():
    inp31 = StringVar()
    inp31 = text3.get('1.0', 'end-1c')
    inp31 = int(inp31)
    inp32 = inp31**(1/2)
    label6.config(text= inp32)
    print('√',inp31,' = ',inp32)

def cbrt():
    inp41 = StringVar()
    inp41 = text4.get('1.0', 'end-1c')
    inp41 = int(inp41)
    inp42 = inp41**(1/3)
    label8.config(text= inp42)
    print('∛',inp41,' = ',inp42)

def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    text3.delete(1.0,END)
    text4.delete(1.0,END)
    label2.config(text='')
    label4.config(text='')
    label6.config(text='')
    label8.config(text='')

title1 = Label(wn, text='Square',font=font)
label1 = Label(wn, text='Number: ',font=font)
text1 = Text(wn, width='25', height='1')
button1 = Button(wn,text='^2',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=square)
label2 = Label(wn, text='',font=font)

title1.grid(row=0, column=1, pady=2)
label1.grid(row=1, column=0, pady=2)
text1.grid(row=1, column=1, pady=2)
button1.grid(row=2, column=0, pady=2)
label2.grid(row=2, column=1, pady=2)


title2 = Label(wn, text=' Cube',font=font)
label3 = Label(wn, text='Number: ',font=font)
text2 = Text(wn, width='25', height='1')
button2 = Button(wn,text='^3',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=cube)
label4 = Label(wn, text='',font=font)

title2.grid(row=4, column=1, pady=2)
label3.grid(row=5, column=0, pady=2)
text2.grid(row=5, column=1, pady=2)
button2.grid(row=7, column=0, pady=2)
label4.grid(row=7, column=1, pady=2)

title3 = Label(wn, text=' Square Root',font=font)
label5 = Label(wn, text='Number: ',font=font)
text3 = Text(wn, width='25', height='1')
button3 = Button(wn,text='√',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=sqrt)
label6 = Label(wn, text='',font=font)

title3.grid(row=9, column=1, pady=2)
label5.grid(row=10, column=0, pady=2)
text3.grid(row=10, column=1, pady=2)
button3.grid(row=12, column=0, pady=2)
label6.grid(row=12, column=1, pady=2)

title4 = Label(wn, text=' Cube Root',font=font)
label7 = Label(wn, text='Number: ',font=font)
text4 = Text(wn, width='25', height='1')
button4 = Button(wn,text='∛',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=cbrt)
label8 = Label(wn, text='',font=font)

title4.grid(row=14, column=1, pady=2)
label7.grid(row=15, column=0, pady=2)
text4.grid(row=15, column=1, pady=2)
button4.grid(row=17, column=0, pady=2)
label8.grid(row=17, column=1, pady=2)


button5 = Button(wn,text='Clear',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=clear)

button5.grid(row=21, column=1, pady=2)


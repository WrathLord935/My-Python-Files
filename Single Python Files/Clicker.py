from tkinter import *
import tkinter.font as font

wn = Tk(className=' Clicker')
wn.geometry('170x230')

font=font.Font(family='Times New Roman', size=24)

global num
global num2
num =  0
num2 =  0

def clear():
    global num
    num = 0
    ClickedNo.config(text = num)
    print('\n-----------------------------------------------------------------------------------------------------------------------------\n                                                                   RESET\n-----------------------------------------------------------------------------------------------------------------------------\n')

def click():
    global num
    global num2
    num2 = num2 + 1
    num = num + 1
#    print('Number of times Clicked: ', num)
#    print('Total number of times Clicked: ', num2)
#    print('')
    ClickedNo.config(text = num)

Clicker = Label(wn, text='Clicker',font=font)
ClickMe = Button(wn,text='Click Me',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=click)
ClickedNo = Label(wn, text=num,font=font)
Clear = Button(wn,text='Clear',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=clear)

Clicker.grid(row=0, column=1, pady=2)
ClickMe.grid(row=2, column=1, pady=2)
ClickedNo.grid(row=3, column=1, pady=2)
Clear.grid(row=4, column=1, pady=2)

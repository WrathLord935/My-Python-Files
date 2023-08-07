#Converting Binary to Decimal and Vice-Versa using Tkinter

#Importing Tkinter
from tkinter import *
import tkinter.font as font

#Creating the GUI
wn = Tk(className=' Binary and Decimal Number System')
wn.geometry('570x380')

#Setting a custom icon
photo = PhotoImage(file = "Tkinter Binary.png")
wn.iconphoto(True, photo)

#Setting the font
font=font.Font(family='Times New Roman', size=14)

#Making clear funtion
def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    label3.config(text='')
    label6.config(text='')

#Making decimal to binary funtion
def convert_binary():
    input1 = StringVar()
    input1 = text1.get('1.0', 'end-1c')
    input1 = int(input1)
    binary_number=format(input1, '8b')
    label3.config(text= binary_number)
    print(input1,' =',binary_number)

#Making binary to decimal funtion
def convert_decimal():
    input2 = ''
    input2 = text2.get('1.0', 'end-1c')
    input3 = list(input2.split(" "))
    value = 0

    for i in range(len(input3)):
        digit = input3.pop()
        if digit == '1':
            value = value + pow(2, i)
    label6.config(text= value)
    print(input2,' = ',value)

#Creating widgets for 'Decimal to Binary'
title1 = Label(wn, text='DECIMAL TO BINARY',font=font)
label1 = Label(wn, text='Decimal Number: ',font=font)
text1 = Text(wn, width='50', height='1')
note1 = Label(wn, text='Note: Don\'t use Space after every digit ',font=font,fg='red')
button1 = Button(wn,text='Convert',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=convert_binary)
label2 = Label(wn, text='Converted: ',font=font)
label3 = Label(wn, text='',font=font)

#Aligning 'Decimal to Binary' widgets
title1.grid(row=0, column=1, pady=2)
label1.grid(row=1, column=0, pady=2)
text1.grid(row=1, column=1, pady=2)
note1.grid(row=2, column=1, pady=2)
button1.grid(row=3, column=0, pady=2)
label2.grid(row=4, column=0, pady=2)
label3.grid(row=4, column=1, pady=2)

#Creating widgets for 'Binary to Decimal'
title2 = Label(wn, text=' BINARY TO DECIMAL',font=font)
label4 = Label(wn, text='Binary Number: ',font=font)
text2 = Text(wn, width='50', height='1')
note1 = Label(wn, text='Note: Use Space after every digit ',font=font,fg='red')
button2 = Button(wn,text='Convert',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=convert_decimal)
label5 = Label(wn, text='Converted: ',font=font)
label6 = Label(wn, text='',font=font)

#Aligning 'Binary to Decimal' widgets
title2.grid(row=6, column=1, pady=2)
label4.grid(row=7, column=0, pady=2)
text2.grid(row=7, column=1, pady=2)
note1.grid(row=8, column=1, pady=2)
button2.grid(row=9, column=0, pady=2)
label5.grid(row=10, column=0, pady=2)
label6.grid(row=10, column=1, pady=2)

#Creating the Clear button
button3 = Button(wn,text='Clear',bg='DeepSkyBlue2',fg='white',activebackground='DeepSkyBlue4',activeforeground='gray',font=font,command=clear)

#Aligning the Clear button
button3.grid(row=11, column=1, pady=2)

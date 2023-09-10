#Importing Modules
import numpy as np

loop = True
line_separator = '\n'

#Functions
def addition(z1,z2):
    z3 = z1 + z2
    real = z3.real
    imaginary = z3.imag
    if (real).is_integer:
        real = int(real)
    if (imaginary).is_integer:
        imaginary = int(imaginary)

    print(f'{z1} + {z2} = {z3}, Where {real} is the real part and {imaginary} is the imaginary part')

def subtraction(z1,z2):
    z3 = z1 - z2
    real = z3.real
    imaginary = z3.imag
    if (real).is_integer:
        real = int(real)
    if (imaginary).is_integer:
        imaginary = int(imaginary)

    print(f'{z1} - {z2} = {z3}, Where {real} is the real part and {imaginary} is the imaginary part')

def multiplication(z1,z2):
    z3 = z1 * z2
    real = z3.real
    imaginary = z3.imag
    if (real).is_integer:
        real = int(real)
    if (imaginary).is_integer:
        imaginary = int(imaginary)

    print(f'{z1} * {z2} = {z3}, Where {real} is the real part and {imaginary} is the imaginary part')

def division(z1,z2):
    z3 = z1 / z2
    real = z3.real
    imaginary = z3.imag
    if (real).is_integer:
        real = int(real)
    if (imaginary).is_integer:
        imaginary = int(imaginary)

    print(f'{z1} / {z2} = {z3}, Where {real} is the real part and {imaginary} is the imaginary part')

def conjugate(z1,z2):
    zc1 = np.conj(z1)
    zc2 = np.conj(z2)

    real1 = zc1.real
    imaginary1 = zc1.imag
    if (real1).is_integer:
        real1 = int(real1)
    if (imaginary1).is_integer:
        imaginary1 = int(imaginary1)

    real2 = zc2.real
    imaginary2 = zc2.imag
    if (real2).is_integer:
        real2 = int(real2)
    if (imaginary2).is_integer:
        imaginary2 = int(imaginary2)

    print(f'Conjugate of {z1} is {zc1}, Where {real1} is the real part and {imaginary1} is the imaginary part')
    print(f'Conjugate of {z2} is {zc2}, Where {real2} is the real part and {imaginary2} is the imaginary part')

#Reapeting Loop
while loop:
    #Inputing Values
    z1 = input('Enter First Complex Number (Use Space before the expression but never after): ')
    z2 = input('Enter Second Complex Number (Use Space before the expression but never after): ')
    print('Which operation would you like to do? Use only the numbers assigned','1.Addition','2.Subtraction','3.Multiplication','4.Division','5.Conjugate',sep='\n\t')
    op = int(input(''))


    if 'i' in z1 and 'i' in z2:

        #Processing inputs
        if '+' in z1:
            x1 = z1.split(' +')
            neg1 = False
        elif '-' in z1:
            x1 = z1.split(' -')
            neg1 = True

        if 'i' in x1[0]:
            a1 = x1[1]
            b1 = x1[0]
            b1 = b1.replace('i','',1)
        elif 'i' in x1[1]:
            a1 = x1[0]
            b1 = x1[1]
            b1 = b1.replace('i','',1)

        a1 = int(a1)
        b1 = int(b1)

        if neg1 == True:
            b1 = b1*-1

        if '+' in z2:
            x2 = z2.split(' +')
            neg2 = False
        elif '-' in z2:
            x2 = z2.split(' -')
            neg2 = True

        if 'i' in x2[0]:
            a2 = x2[1]
            b2 = x2[0]
            b2 = b2.replace('i','',1)
        elif 'i' in x2[1]:
            a2 = x2[0]
            b2 = x2[1]
            b2 = b2.replace('i','',1)
          
        a2 = int(a2)
        b2 = int(b2)

        if neg2 == True:
            b2 = b2*-1

        #Making Complex Number Variables Using Processed Variables 
        z1 = complex(a1,b1)
        z2 = complex(a2,b2)

        #Doing Operations
        if op == 1:
            addition(z1,z2)
        elif op == 2:
            subtraction(z1,z2)
        elif op == 3:
            multiplication(z1,z2)
        elif op == 4:
            division(z1,z2)
        elif op == 5:
            conjugate(z1,z2)
        else:
            print('Error in choosing operator')
            
    else:
        print('Input isnt a complex number')

    loop = (input(f'Run Again?(Y/N){line_separator}').lower() == "y")

print(f'Thank you and Goodbye{line_separator}\tCreated by Wrath Lord')

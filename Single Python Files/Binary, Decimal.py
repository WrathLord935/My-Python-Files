#Converting Binary to Decimal and Vice-Versa


h = 'Y'
while h == 'Y' or h == 'y':
    a = int(input('Choose:\n\t1.Decimal to Binary\n\t2.Binary to Decimal\n'))
    
    if a == 1:
        d_num = int(input('Enter a Number: '))
        value = format(d_num, '8b')
        print('The binary value of the decimal number',d_num,' is', value)

    if a == 2:
        b_num = input("Input a binary number: ")
        b_num2 = b_num
        value = 0
        b_num = list(b_num)

        for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                value = value + pow(2, i)
        print('The decimal value of the binary number',b_num2,' is', value)


    h = input('Run Again?(Y/N)\n')

while h == 'N' or h == 'n':
    print('Thank you and Goodbye\n\tCreated by Wrath Lord')
    break

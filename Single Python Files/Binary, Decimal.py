#Converting Binary to Decimal and Vice-Versa

loop = True
while loop:
    a = input('Choose:\n\t1.Decimal to Binary\n\t2.Binary to Decimal\n')
    q = 0

    for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        if i in a:
            q = 1

    if q == 1:
        print('Enter Numbers Only')
    else:
        a = int(a)
    
        
        if a == 1:
            z = 0
            d_num = input('Enter a Number: ')

            for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                if i in d_num:
                    z = 1

            if z == 1:
                print('Enter Numbers Only')
            else:
                d_num = int(d_num)        
                value = format(d_num, '8b')
                print('The binary value of the decimal number',d_num,' is', value)

        if a == 2:
            z = 0
            x = 0
            b_num = input("Input a binary number: ")
            b_num2 = b_num
            value = 0

            for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                if i in b_num:
                    z = 1

            if z == 1:
                print('Enter Numbers Only')
            else:
                for j in ['2','3','4','5','6','7','8','9']:
                    if j in b_num:
                        print('Enter Only Zeros and Ones')
                        x = 1

                if x == 0:
                    b_num = list(b_num)
                            

                    for i in range(len(b_num)):
                        digit = b_num.pop()
                        if digit == '1':
                                    value = value + pow(2, i)
                    print('The decimal value of the binary number',b_num2,'is', value)

        else:
            print('Choose a Given Option')

    
    loop =  input('Run Again?(Y/N)\n').lower() == 'y'

print('Thank you and Goodbye\n\tCreated by Wrath Lord')
